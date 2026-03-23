# ТЗ: input-структура и intake-helper для проекта на OpenCode + AI Factory

## 1. Цель intake-слоя

Сделать входные данные:
- полными,
- воспроизводимыми,
- пригодными для повторного запуска pipeline,
- независимыми от Google Sheets.

Intake-helper не генерирует финальные маркетинговые артефакты. Он только:
- собирает сырой ввод,
- задает недостающие вопросы,
- нормализует ответы,
- валидирует полноту,
- сохраняет в строгие файлы.

Это не избыточно. Это обязательный слой. Без него будет мусорный input и нестабильный output.

## 2. Non-goals

Intake-helper не должен:
- сам “додумывать” бизнес вместо пользователя;
- генерировать финальные сегменты, JTBD, скрипты и т.д.;
- требовать заполнить 100% полей до старта;
- превращаться в длинный чат на 30 вопросов.

Его задача — добрать критический минимум и пометить пробелы.

## 3. Структура проекта

```text
project-root/
├── .ai-factory/
│   ├── DESCRIPTION.md
│   ├── ARCHITECTURE.md
│   ├── PLAN.md
│   └── references/
├── .opencode/
│   ├── agents/
│   │   ├── intake.md
│   │   ├── researcher.md
│   │   ├── interviewer.md
│   │   ├── sales-architect.md
│   │   └── validator.md
│   └── plugins/
├── opencode.json
├── inputs/
│   ├── raw/
│   │   ├── product.md
│   │   ├── company.md
│   │   ├── audience.md
│   │   ├── tone.md
│   │   └── constraints.md
│   ├── normalized/
│   │   ├── product.yaml
│   │   ├── company.yaml
│   │   ├── audience.yaml
│   │   ├── sales.yaml
│   │   ├── tone.yaml
│   │   └── homework.yaml
│   └── validation/
│       ├── completeness.json
│       ├── contradictions.json
│       └── warnings.md
├── schemas/
│   ├── product.schema.json
│   ├── company.schema.json
│   ├── audience.schema.json
│   ├── sales.schema.json
│   └── tone.schema.json
├── prompts/
│   ├── intake/
│   └── pipeline/
├── pipelines/
│   ├── homework_marketing.yaml
│   ├── homework_custdev_sales.yaml
│   └── expert_mode.yaml
├── runs/
├── outputs/
│   ├── json/
│   ├── md/
│   ├── csv/
│   └── xlsx/
└── docs/
```

## 4. Обязательные input-файлы

### 4.1 `inputs/raw/product.md`
Свободный текст. Пользователь пишет как умеет.

Минимум:
- что за продукт;
- для кого;
- какую проблему решает;
- что продается;
- как сейчас это продается;
- в чем предполагаемая ценность.

### 4.2 `inputs/raw/company.md`
Минимум:
- кто мы;
- что продаем;
- кому продаем;
- B2B/B2C;
- желаемый результат от продаж.

### 4.3 `inputs/raw/audience.md`
Минимум:
- кого считаем ЦА;
- по каким признакам;
- какие боли предполагаем;
- кто сейчас покупает, если уже есть опыт.

### 4.4 `inputs/raw/tone.md`
Минимум:
- стиль коммуникации;
- запрещенные формулировки;
- допустимый уровень напора;
- “на вы” / “на ты”;
- отраслевой контекст.

### 4.5 `inputs/raw/constraints.md`
Минимум:
- язык ответа;
- география;
- лимит длины;
- запрещенные допущения;
- формат выхода;
- надо ли делать экспорт под Google Sheets.

## 5. Нормализованные input-файлы

### 5.1 `inputs/normalized/product.yaml`

```yaml
product:
  name: ""
  one_liner: ""
  full_description: ""
  category: ""
  market_type: ""            # B2B | B2C | B2B2C
  problem_statement: ""
  solution_statement: ""
  core_value: ""
  usp_candidates: []
  features: []
  benefits: []
  pricing_model: ""
  price_range: ""
  delivery_model: ""
  geography: []
  competitors_known: []
  evidence_available: false
```

### 5.2 `inputs/normalized/company.yaml`

```yaml
company:
  brand_name: ""
  description: ""
  industry: ""
  business_model: ""
  offer: ""
  deal_type: ""              # one-off | subscription | service | enterprise
  average_check: ""
  sales_cycle: ""
  target_regions: []
  proof_assets: []           # кейсы, демо, отзывы
  next_step_goal: ""         # demo | call | КП | pilot
```

### 5.3 `inputs/normalized/audience.yaml`

```yaml
audience:
  suspected_core_audience: ""
  current_customers: []
  buyer_type: ""             # end-user | operator | manager | owner
  decision_context: ""
  languages: []
  regions: []
  income_level_hint: ""
  roles_or_professions: []
  interests: []
  pains: []
  fears: []
  needs: []
  desired_outcomes: []
```

### 5.4 `inputs/normalized/sales.yaml`

```yaml
sales:
  target_company_types: []
  target_titles: []
  desired_lpr_profiles: 3
  outreach_channel: ""       # phone | email | linkedin | mixed
  objection_sensitivity: ""  # low | medium | high
  call_goal: ""
  hard_constraints: []
```

### 5.5 `inputs/normalized/tone.yaml`

```yaml
tone:
  language: "ru"
  politeness: "formal"
  person: "2nd"
  confidence_level: "measured"
  verbosity: "short"
  banned_phrases: []
  preferred_patterns: []
  examples_good: []
  examples_bad: []
```

### 5.6 `inputs/normalized/homework.yaml`

```yaml
homework:
  need_marketing_sheet: true
  need_custdev_chain: true
  need_lpr_chain: true
  need_sales_script: true
  export_google_sheets_ready: true
  replace_formulas_with_values: true
```

## 6. Классы полей

Каждое поле должно иметь статус:
- `required` — без него этап не стартует;
- `recommended` — этап стартует, но helper выдает warning;
- `optional` — просто сохраняется.

### Required для первой лекции
- `product.full_description`
- `product.problem_statement`
- `product.market_type`
- `audience.suspected_core_audience`

### Required для второй лекции: кастдев
- все выше +
- `audience.pains` или `audience.needs`
- `product.core_value`

### Required для второй лекции: ЛПР
- `company.offer`
- `company.industry`
- `sales.target_company_types`
- `sales.target_titles` или пусто с флагом auto-discover

### Required для скрипта
- `company.brand_name`
- `company.offer`
- `sales.outreach_channel`
- `sales.call_goal`
- `tone.language`
- `tone.politeness`

## 7. Логика intake-helper

### 7.1 Общий режим
Helper работает в 4 фазах:

1. `ingest`  
   Читает `raw/*.md`, извлекает кандидаты полей.

2. `gap-analysis`  
   Определяет:
   - что заполнено,
   - чего не хватает,
   - что противоречиво,
   - что подозрительно расплывчато.

3. `guided-questions`  
   Задает только недостающие вопросы. Не больше 10 за проход.

4. `normalize-and-save`  
   Обновляет `normalized/*.yaml` + пишет отчеты в `inputs/validation/`.

### 7.2 Поведение
Helper обязан:
- задавать короткие вопросы;
- группировать вопросы по блокам;
- не спрашивать то, что уже есть;
- не плодить креатив;
- явно маркировать допущения;
- сохранять source trace: откуда взято поле — `raw`, `user_answer`, `inferred`.

### 7.3 Stop condition
Helper завершает intake, если:
- все `required` поля заполнены;
- нет критических противоречий;
- warnings только уровня `recommended`.

## 8. Правила валидации

### 8.1 Полнота
Пример:
- `product.full_description` < 300 символов → warning
- `audience.pains` пустой → warning или blocker для кастдева
- `sales.call_goal` пустой → blocker для скрипта

### 8.2 Противоречия
Пример:
- `market_type=B2B`, но `target_company_types=[]` и `roles_or_professions` только consumer-level
- `pricing_model=enterprise`, но `average_check=низкий` без пояснения
- `tone.politeness=formal`, но `preferred_patterns` содержат агрессивный разговорный стиль

### 8.3 Расплывчатость
Helper должен помечать как weak:
- “для всех”
- “любому бизнесу”
- “автоматизирует всё”
- “дешево/быстро/качественно” без конкретики

## 9. Роли агентов в OpenCode

### `intake`
Задача:
- извлечение и нормализация input;
- постановка уточняющих вопросов;
- первичная валидация.

Модель:
- `openai/gpt-5.4-mini`

### `validator`
Задача:
- schema check;
- contradiction check;
- completeness report.

Модель:
- `openai/gpt-5.4-nano` или `mini`

### `researcher`
Задача:
- продукт;
- ядро ЦА;
- сегменты;
- deep-dive;
- гипотезы.

Модель:
- `openai/gpt-5.4`

### `interviewer`
Задача:
- вопросы по кастдеву;
- симуляция аватаров;
- synthesis из реальных интервью.

Модель:
- `openai/gpt-5.4`

### `sales-architect`
Задача:
- компании;
- ЛПР;
- блоки скрипта;
- стилизация.

Модель:
- `openai/gpt-5.4`

## 10. Маршрутизация моделей

Роутинг:
- extraction / classification / checklist → `nano`
- intake / reformat / concise rewrite → `mini`
- research / segmentation / hypotheses / LPR / script blocks → `gpt-5.4`

## 11. Конфигурационная политика

### `opencode.json`
Должен задавать:
- OpenAI как enabled provider;
- default model = `openai/gpt-5.4`
- small_model = `openai/gpt-5.4-mini`
- custom agents;
- instructions files.

### `.ai-factory/`
Использовать по назначению:
- `DESCRIPTION.md` — что делает система;
- `ARCHITECTURE.md` — стадии intake/pipeline/export;
- `PLAN.md` — текущий plan;
- `references/` — конспекты лекций, выжимка по xlsx, правила формул и структуры.

## 12. Что helper должен спрашивать

Порядок вопросов:

### Блок A. Продукт
1. Что именно продается?
2. Какую проблему это решает?
3. Для кого это в первую очередь?
4. B2B, B2C или смешанная модель?
5. Какой ожидаемый следующий шаг от клиента?

### Блок B. Аудитория
6. Кто уже покупал или кто, по твоему мнению, должен покупать?
7. Какие 3 главные боли?
8. Какой желаемый результат у клиента после покупки?

### Блок C. Продажи
9. Через какой канал будет outreach?
10. На кого хочешь выходить: роли/должности?

Если после этого обязательные поля собраны — helper останавливается.

## 13. Формат validation report

`inputs/validation/completeness.json`

```json
{
  "status": "partial",
  "ready_for": ["homework_marketing", "custdev"],
  "blocked_for": ["sales_script"],
  "missing_required": [
    "sales.call_goal",
    "company.brand_name"
  ],
  "weak_fields": [
    "audience.suspected_core_audience"
  ]
}
```

`inputs/validation/warnings.md`

```md
- Поле `suspected_core_audience` слишком широкое: "малый и средний бизнес"
- Не указан `call_goal`, поэтому скрипт продаж не может быть целевым
- `pricing_model` не согласуется с `average_check`
```

## 14. Acceptance criteria

Слой intake считается готовым, если:
- из сырых текстов можно получить валидный `normalized/`;
- helper задает только недостающие вопросы;
- после 1–2 проходов можно запускать pipeline без ручной правки структуры;
- один и тот же input стабильно запускает одну и ту же цепочку;
- финальные данные годятся и под ДЗ, и под будущие экспертизы.

## 15. Конструктивная обратная связь по идее

Сильные стороны:
- отделение сбора input от генерации output;
- проект становится переиспользуемым;
- легче дебажить и масштабировать;
- можно подсовывать реальные интервью позже, не ломая архитектуру.

Слабые места, если сделать небрежно:
- helper начнет “умничать” и фантазировать;
- YAML разрастется до монстра;
- появится дублирование между `product`, `company`, `audience`;
- вся система станет медленной и дорогой.

Правильный баланс:
- строгие шаблоны;
- короткий intake wizard;
- валидатор;
- минимум магии;
- основная генерация только после intake.

Это не overengineering. Это нормальный фундамент.

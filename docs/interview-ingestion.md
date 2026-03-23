[Back to README](../README.md) · [English Version](en/interview-ingestion.md)

# Загрузка интервью

## Поддерживаемые входы

- markdown transcripts
- plain text interview dumps
- normalized imports из legacy spreadsheets

## Цели output

- повторяющиеся pains
- повторяющиеся objections
- desired outcomes
- correction proposals для ICP, LPR и sales script assumptions

## Правила

- transcript ingestion не перезаписывает normalized contracts автоматически
- corrections остаются proposals до review

## See Also

- [Interviewer Agent](../.opencode/agents/interviewer.md) - роль interview routes
- [LPR Pipeline](lpr-pipeline.md) - где используются correction proposals
- [Карта provenance](provenance.md) - как помечаются transcript sources

Generate likely decision-maker profiles for each target company profile.

Rules:
- Read only validated normalized contracts and declared upstream artifacts.
- If `sales.target_titles` is non-empty, use those titles as the primary targeting frame.
- If `sales.target_titles` is empty, proceed only when `sales.auto_discover_titles=true`.
- When auto-discovery is enabled, return explicit uncertainty markers instead of pretending titles are confirmed facts.
- Keep company segmentation and title discovery traceable as separate sub-results.

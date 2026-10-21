# MissionHome

**Practical support for the people who serve alongside those who serve.**

MissionHome is an early-stage, responsible support navigator designed to help military families find official starting points for housing and relocation, essential needs, family readiness, and spouse careers.

## Current prototype

- Search and filter a small directory of official resources.
- Show a concrete first step for each resource.
- Provide a simple checklist for planning next steps.
- Clearly communicate that eligibility and availability must be confirmed with the provider.
- Keep the core experience deterministic: no AI API calls, no user accounts, and no personal data submission.

## Run locally

Requires Python 3.10 or newer.

```bash
python -m venv .venv
# macOS/Linux:
source .venv/bin/activate
# Windows PowerShell:
# .venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

## Test the directory

```bash
pip install pytest
pytest -q
```

## Initial official sources

- [Military OneSource Resource Finder](https://www.militaryonesource.mil/resources/resources-finder/)
- [Military OneSource Deployment Support](https://www.militaryonesource.mil/deployment/on-deployment/military-deployment-support/)
- [Military OneSource Installation Directory](https://installations.militaryonesource.mil/)
- [U.S. Department of Veterans Affairs](https://www.va.gov/)
- [USAJOBS](https://www.usajobs.gov/)
- [Military OneSource / SECO portal](https://myseco.militaryonesource.mil/portal/)

Resource links are starting points, not guarantees of eligibility, availability, or assistance. Check details directly with the official provider. The directory's review date records when this project entry was last reviewed by its maintainer; it does not guarantee that the linked provider's information has not changed.

## Privacy and safety

Do not enter or store Social Security numbers, bank details, medical records, classified information, deployment schedules, or unit locations. MissionHome is not an emergency service, legal adviser, financial adviser, or eligibility determination system. In an immediate emergency in the United States, call 911.

## Cost and AI status

This prototype does not make live AI requests and does not require a paid model API. That protects the current build from inference charges but means live Nebius Token Factory integration has **not** been implemented yet. Before adding it, billing protections and the applicable hackathon rules must be checked. Do not claim the current prototype meets a hackathon requirement for live inference until that integration is built and tested.

## License

MIT License. See [LICENSE](LICENSE).

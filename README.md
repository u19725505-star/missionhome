# MissionHome

**Practical support for the people who serve alongside those who serve.**

MissionHome is an early-stage, responsible support navigator designed to help military families find official starting points for housing and relocation, food and essential needs, financial support, family readiness, and spouse careers.

## Current prototype

- Search and filter a directory of official starting points.
- Show a concrete first step for each resource.
- Cover food assistance, financial counseling, family readiness, relocation, veteran services, and spouse employment.
- Provide a simple checklist for planning next steps.
- Clearly communicate that eligibility and availability must be confirmed with the provider.
- Keep the core experience deterministic: no AI API calls, no user accounts, and no personal data submission.

## Public demo

- Live app: https://missionhome.onrender.com
- Reviewer walkthrough and smoke tests: [docs/HACKATHON_DEMO.md](docs/HACKATHON_DEMO.md)

## Run locally

Requires Python 3.10 or newer.

```bash
python -m venv .venv
# macOS/Linux:
source .venv/bin/activate
# Windows PowerShell:
# .venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

## Test the directory

```bash
pip install pytest
pytest -q
```

Tests check required resource fields, HTTPS URL structure, unique names, usable categories and keywords, ISO-formatted review dates, and coverage of core support areas. These checks do not guarantee that external sites are available or that any individual is eligible for assistance.

## Initial official sources

- [Military OneSource Resource Finder](https://www.militaryonesource.mil/resources/resources-finder/)
- [Military OneSource Food Assistance for Military Families](https://www.militaryonesource.mil/resources/millife-guides/food-security-resources-and-support-programs/)
- [Military OneSource Financial Counseling](https://www.militaryonesource.mil/benefits/financial-counseling/)
- [Military & Family Life Counseling](https://www.militaryonesource.mil/programs/military-family-life-counseling/)
- [Military OneSource Deployment Support](https://www.militaryonesource.mil/deployment/on-deployment/military-deployment-support/)
- [Military OneSource Installation Directory](https://installations.militaryonesource.mil/)
- [U.S. Department of Veterans Affairs](https://www.va.gov/)
- [USAJOBS](https://www.usajobs.gov/)
- [Military OneSource / SECO portal](https://myseco.militaryonesource.mil/portal/)

Resource links are starting points, not guarantees of eligibility, availability, or assistance. Check details directly with the official provider. The directory's review date records when this project entry was last reviewed by its maintainer; it does not guarantee that the linked provider's information has not changed.

## Privacy and safety

Do not enter or store Social Security numbers, bank details, medical records, classified information, deployment schedules, or unit locations. MissionHome is not an emergency service, legal adviser, financial adviser, or eligibility determination system. In an immediate emergency in the United States, call 911. For a mental health crisis in the United States, call or text 988.

## Cost and AI status

This prototype does not make live AI requests and does not require a paid model API. That protects the current build from inference charges but means live Nebius Token Factory integration has **not** been implemented yet. Before adding it, billing protections and the applicable hackathon rules must be checked. Do not claim the current prototype meets a hackathon requirement for live inference until that integration is built and tested.

## License

MIT License. See [LICENSE](LICENSE).

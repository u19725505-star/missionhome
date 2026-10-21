# MissionHome Demo and Validation Checklist

## Public demo

- App: https://missionhome.onrender.com
- Repository: https://github.com/u19725505-star/missionhome

## Suggested 2-minute walkthrough

1. **Start with the problem.** Military families can face overlapping housing, food, financial, relocation, family-readiness, and employment challenges. Finding a trustworthy starting point can be confusing.
2. **Show the directory.** Point out that each card names its source owner, explains a first step, and links directly to an official resource.
3. **Demonstrate category filtering.** Select **Food & essential needs** and then **Financial support**. Confirm the result count and visible cards change.
4. **Demonstrate search.** Search for terms such as `SNAP`, `budget`, `deployment`, or `spouse`. Clear the search and show the full directory again.
5. **Show the safety boundary.** Select the immediate-danger option to display emergency guidance. Explain that MissionHome is a navigation aid, not an emergency service or an eligibility decision-maker.
6. **Show the next-step checklist.** Mark one or more steps and use the progress button.
7. **Close with the trust model.** The prototype does not ask users to submit personal details and makes no live AI/API calls.

## Manual smoke-test checklist

- [ ] Public URL loads on mobile Safari and desktop.
- [ ] All areas shows the complete directory.
- [ ] Each support category filters to the expected cards.
- [ ] Search terms match names, categories, descriptions, and keywords.
- [ ] A nonsense search produces a helpful no-results message.
- [ ] Immediate danger shows the 911 / 988 notice.
- [ ] Each resource link opens the intended official provider.
- [ ] The checklist progress count updates correctly.
- [ ] No form requests sensitive personal information.

## Automated tests

From the repository root:

```bash
python -m pip install -r requirements.txt
python -m pip install pytest
pytest -q
```

The tests validate required fields, HTTPS URL structure, unique resource names, usable categories and keywords, ISO review dates, and coverage of core support areas. They do not prove that third-party pages are always available or that any user is eligible for a program.

## Honest status for reviewers

- **Implemented:** Streamlit directory, category filter, keyword search, official-source links, emergency notice, checklist, resource data tests.
- **Privacy boundary:** No account, no collection of sensitive user details, no AI request in the current version.
- **Not implemented:** Live Nebius Token Factory inference.
- **Do not claim:** that the current prototype satisfies a live-inference requirement, that every external link is continuously monitored, or that a user qualifies for any listed program.

Keep the prototype within the project's $0 out-of-pocket constraint. Do not enable chargeable model calls or upgrade hosting unless billing protections and budget approval are explicitly confirmed.

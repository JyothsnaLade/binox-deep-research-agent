def retrieve_docs(query):
    if "economic" in query:
        return [
            "High production costs in US due to labor",
            "China benefits from economies of scale",
            "EU investing in local battery production"
        ]

    elif "risk" in query:
        return [
            "Geopolitical tensions affect supply chains",
            "Dependency on China for lithium processing",
            "Trade restrictions impact battery exports"
        ]

    elif "regional" in query:
        return [
            "China dominates battery manufacturing",
            "US focuses on domestic supply chain resilience",
            "EU emphasizes sustainability regulations"
        ]

    else:
        return ["General EV supply chain insight"]
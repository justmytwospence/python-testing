with open("techcrunch.csv") as file:
    lines_list = (line.strip().split(",") for line in file)
    columns = next(lines_list)
    companies_dict = (dict(zip(columns, field)) for field in lines_list)
    funding = (
        int(company["raisedAmt"])
        for company in companies_dict
        if company["round"] == "a")
    print(sum(funding))
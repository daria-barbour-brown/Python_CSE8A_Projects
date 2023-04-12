from CSE8ACSV import *
import matplotlib.pyplot as plot


tech_diversity_data = get_diversity_data("tech_diversity.csv")


def get_avg_pcnt_category_overall(category):
    total = 0
    for company in tech_diversity_data:
        total += tech_diversity_data[company][category]
    return total / len(tech_diversity_data)

def get_all_companies():
    return list(tech_diversity_data.keys())


def get_all_companies1():
    #for loop to get keys
    lst = []
    for company in tech_diversity_data:
        lst.append(company)
    return lst


def def_all_categories():
    for item in tech_diversity_data.items():
        return list(item[1].keys())
    return None


def def_all_categories1():
    #nested for loop
    for key in tech_diversity_data:
        return list(tech_diversity_data[key].keys())
    return None


def def_all_categories2():
    companies = get_all_companies()
    if len(companies) == 0:
        return None
    company = companies[0]
    return list(tech_diversity_data[company].keys())


#not general enough
##def def_all_categories3():
##    lst = []
##    for i in tech_diversity_data['Nvidia']:
##        lst.append(i)
##    return lst


def plot_categories_in_company(company, categories):
    values = []
    for category in categories:
        values.append(tech_diversity_data[company][category])
    print(categories)
    print(values)
    plot.bar(categories, values)
    plot.xlabel("Category of People")
    plot.ylabel("Percentage of People")
    plot.title("Diversity of people at " + company)
    plot.show()


def plot_category_across_companies(category, companies):
    values = []
    for company in companies:
        values.append(tech_diversity_data[company][category])
    plot.bar(companies, values)
    plot.xlabel("Companies")
    plot.ylabel("Percentage of People")
    plot.title("Representation of " + category + " people in tech companies")
    plot.show()










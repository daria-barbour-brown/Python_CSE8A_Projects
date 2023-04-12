from CSE8ACSV import *
import matplotlib.pyplot as plot

tech_diversity_data = get_diversity_data("tech_diversity.csv")

def plot_category_across_companies(category, companies):
    values = []

    for company in companies:
        data = tech_diversity_data[company][category]
        values.append(data)
    
    print(values)

    plot.bar(companies, values)
    #plot.pie(values, labels=companies)

    plot.xlabel("Companies")
    plot.ylabel("Percentage of people")
    plot.title("Representation of " + category + " people in tech companies")

    plot.show()

#Sample run
#>>> plot_category_across_companies("black", ["Google", "Cisco", "Facebook"])
#['Google', 'Cisco', 'Facebook']
#[2.4, 3.4, 2.3]

plot_category_across_companies("black", ["Google", "Cisco", "Facebook"])
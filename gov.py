from googlesearch import search

def fetch_indian_gov_sites(query, num_results=10):
    search_query = f'site:gov.in {query}'
    indian_gov_sites = []
    for url in search(search_query, num=num_results):
        if '.gov.in' in url:
            indian_gov_sites.append(url)
    return indian_gov_sites

if __name__ == "__main__":
    query = "government of India"
    num_results = 10
    indian_gov_sites = fetch_indian_gov_sites(query, num_results)

    print("Indian Government Websites:")
    for site in indian_gov_sites:
        print(site)

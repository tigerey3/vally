from civic_api import CivicApi
import jmespath

event = CivicApi.voter_query()

def voterInfoQuery(event):
    search_string = "contests[?office == 'U. S. Senator'].candidates | []"
    candidates = jmespath.search(search_string, event)
    print(candidates)
    print(type(candidates))
    # print(event.get("contests")[0].get("candidates")[0].get("name"))
    # print(event_dict)


voterInfoQuery(event)
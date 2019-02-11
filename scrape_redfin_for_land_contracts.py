from redfin import RedFin

start_url = 'https://www.redfin.com/city/5665/MI/Detroit/filter/remarks=land+contract'

redfin = RedFin()
redfin.start_url = start_url
redfin.get_search_results()
redfin.get_property_data()

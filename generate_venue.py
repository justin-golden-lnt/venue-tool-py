import datetime

court_levels = {
'Agency': 'AGCY',
'Apellate (Highest)': 'APHI',
'Apellate (Intermediate)': 'APIM',
'Arbitration Service': 'ARBS',
'Authority': 'AUTH',
'Bankruptcy': 'BANK',
'Board': 'BORD',
'Circuit': 'CIRC',
'Claims': 'CLMS',
'Common Pleas': 'CMPL',
'Criminal': 'CRMN',
'District': 'DIST',
'Family/Domestic Relations': 'FAML',
'Housing': 'HOUS',
'Land': 'LAND',
'Magistrate': 'MAGI',
'Mediation Service': 'MEDI',
'Probate': 'PROB',
'Small Claims': 'SMCL',
'Superior': 'SUPR',
'Unknown': 'UNKN'
}

states = {
'Alabama': 'AL01',
'Alaska': 'AK01',
'Alberta': 'ALBR',
'All States': 'ALLS',
'Arizona': 'AZ01',
'Arkansas': 'AR01',
'British Columbia': 'BRCO',
'California': 'CA01',
'Canada': 'CANA',
'China': 'CHN5',
'Colorado': 'CO01',
'Connecticut': 'CT01',
'Delaware': 'DE01',
'District of Columbia': 'DC01',
'Florida': 'FL01',
'Georgia': 'GA01',
'Guam, US': 'GU01',
'Hawaii': 'HI01',
'Idaho': 'ID01',
'Illinois': 'IL01',
'Indiana': 'INDA',
'Iowa': 'IA01',
'Kansas': 'KS01',
'Kentucky': 'KY01',
'Louisiana': 'LA01',
'Maine': 'ME01',
'Maryland': 'MD01',
'Massachusetts': 'MA01',
'Mexico': 'MEXI',
'Michigan': 'MI01',
'Minnesota': 'MN01',
'Mississippi': 'MISS',
'Missouri': 'MISO',
'Montana': 'MT01',
'Multi-State': 'MU01',
'Nebraska': 'NE01',
'Nevada': 'NV01',
'New Hampshire': 'NH01',
'New Jersey': 'NJ01',
'New Mexico': 'NM01',
'New York': 'NY01',
'Newfoundland and Labrador': 'NFLL',
'North Carolina': 'NC01',
'North Dakota': 'ND01',
'Ohio': 'OH01',
'Oklahoma': 'OK01',
'Ontario': 'ONTR',
'Oregon': 'OR01',
'Pennsylvania': 'PA01',
'Puerto Rico': 'PU01',
'Quebec': 'QBEC',
'Rhode Island': 'RI01',
'South Carolina': 'SC01',
'South Dakota': 'SD01',
'Tennessee': 'TN01',
'Texas': 'TX01',
'Utah': 'UT01',
'Vermont': 'VT01',
'Virgin Islands, US': 'VU01',
'Virginia': 'VA01',
'Washington': 'WA01',
'West Virginia': 'WV01',
'Wisconsin': 'WI01',
'Wyoming': 'WY01'
}

xmlTemplate = """<?xml version="1.0" encoding="UTF-8"?>
<TeamConnectRequest>
	<Authentication>
		<Username>tc_xml</Username>
		<Password>replaceme</Password>
	</Authentication>

	<Contact op="insert" OverrideDuplicateCheck="true">
		<Type>C</Type>
		<DefaultCategory>CONT_EXTL_VENU</DefaultCategory>
		<Name>%(full_name)s</Name>

		<Detail key="CONT_EXTL_VENU">
			<CnVnCounty>%(county)s</CnVnCounty>
			<CnVnLevel>%(court_level_code)s</CnVnLevel>
			<CnVnState>%(state_code)s</CnVnState>
		</Detail>

		<Address key="ADDR_OTHE" action="default">
			<Street></Street>
			<City></City>
			<State>%(state)s</State>
			<PostalCode></PostalCode>
			<County>%(county)s</County>
			<Country></Country>
			<CurrentOn>%(date)s</CurrentOn>
		</Address>
	</Contact>
</TeamConnectRequest>"""

now = datetime.datetime.now()
formated_date = '{}-{}-{}'.format(now.year, now.month, now.day)

full_name = input('Court full name:\n').strip()
county = input('\nCounty:\n').strip()
state = input('\nState:\n').strip()
while state not in states:
	print('\nState not found. Please enter one of the following:')
	print( ', '.join(list(states.keys() ) ) )
	state = input('\nState:\n').strip()
court_level = input('\nCourt Level:\n').strip()
while court_level not in court_levels:
	print('\nCourt Level not found. Please enter one of the following:')
	print( ', '.join(list(court_levels.keys() ) ) )
	court_level = input('\nCourt Level:\n').strip()

data = {
	'full_name': full_name,
	'county': county,
	'state': state,
	'state_code': 'USST_ROOT_' + states[state],
	'court_level_code': 'CTLV_ROOT_' + court_levels[court_level],
	'date': formated_date
}

with open('output.txt', 'w') as f:
	f.write(xmlTemplate%data)

input('\nThe file "output.txt" has been generated. \nPress any key to exit . . .')
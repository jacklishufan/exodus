from .models import *

COUNTRY_DICT = {
}

COUNTRY_ISO = {'ABW': ['Aruba'],
 'AFG': ['Afghanistan'],
 'AGO': ['Angola'],
 'AIA': ['Anguilla'],
 'ALA': ['Åaland Island'],
 'ALB': ['Albania'],
 'AND': ['Andorra'],
 'ARE': ['United Arab Emirates'],
 'ARG': ['Argentina','Argentine'],
 'ARM': ['Armenia'],
 'ASM': ['American Samoa'],
 'ATA': ['Antarctica'],
 'ATF': ['French Southern Territories'],
 'ATG': ['Antigua & Barbuda','Antigua and Barbuda'],
 'AUS': ['Australia'],
 'AUT': ['Austria'],
 'AZE': ['Azerbaijan'],
 'BDI': ['Burundi'],
 'BEL': ['Belgium'],
 'BEN': ['Benin'],
 'BES': ['Caribbean Netherlands'],
 'BFA': ['Burkina'],
 'BGD': ['Bangladesh'],
 'BGR': ['Bulgaria'],
 'BHR': ['Bahrain'],
 'BHS': ['The Bahamas','Bahamas'],
 'BIH': ['Bosnia & Herzegovina','Bosnia and Herzegovina'],
 'BLM': ['Saint Barthélemy'],
 'BLR': ['Belarus'],
 'BLZ': ['Belize'],
 'BMU': ['Bermuda'],
 'BOL': ['Bolivia'],
 'BRA': ['Brazil'],
 'BRB': ['Barbados'],
 'BRN': ['Brunei'],
 'BTN': ['Bhutan'],
 'BVT': ['Bouvet Island'],
 'BWA': ['Botswana'],
 'CAF': ['Central African Republic','Central Africa',],
 'CAN': ['Canada'],
 'CCK': ['Cocos (Keeling) Islands'],
 'CHE': ['Switzerland'],
 'CHL': ['Chile'],
 'CHN': ['China'],
 'CIV': ["Côte d'Ivoire",'Cote d’lvoire'],
 'CMR': ['Cameroon'],
 'COD': ['Democratic Republic of the Congo','Democratic Republic of Congo'],
 'COG': ['Republic of the Congo'],
 'COK': ['Cook Islands'],
 'COL': ['Colombia'],
 'COM': ['The Comoros'],
 'CPV': ['Cape Verde','Cabo Verde'],
 'CRI': ['Costa Rica'],
 'CUB': ['Cuba'],
 'CXR': ['Christmas Island'],
 'CYM': ['Cayman Islands'],
 'CYP': ['Cyprus'],
 'CZE': ['Czech Republic'],
 'DEU': ['Germany'],
 'DJI': ['Djibouti'],
 'DMA': ['Dominica'],
 'DNK': ['Denmark'],
 'DOM': ['Dominican Republic'],
 'DZA': ['Algeria'],
 'ECU': ['Ecuador'],
 'EGY': ['Egypt'],
 'ERI': ['Eritrea'],
 'ESH': ['Western Sahara'],
 'ESP': ['Spain'],
 'EST': ['Estonia'],
 'ETH': ['Ethiopia'],
 'FIN': ['Finland'],
 'FJI': ['Fiji'],
 'FLK': ['Falkland Islands'],
 'FRA': ['France'],
 'FRO': ['Faroe Islands'],
 'FSM': ['Federated States of Micronesia'],
 'GAB': ['Gabon'],
 'GBR': ['Great Britain','United Kingdom','England'],
 'GEO': ['Georgia'],
 'GGY': ['Guernsey'],
 'GHA': ['Ghana'],
 'GIB': ['Gibraltar'],
 'GIN': ['Guinea'],
 'GLP': ['Guadeloupe'],
 'GMB': ['Gambia'],
 'GNB': ['Guinea-Bissau'],
 'GNQ': ['Equatorial Guinea'],
 'GRC': ['Greece'],
 'GRD': ['Grenada'],
 'GRL': ['Greenland'],
 'GTM': ['Guatemala'],
 'GUF': ['French Guiana'],
 'GUM': ['Guam'],
 'GUY': ['Guyana'],
 'HKG': ['Hong Kong'],
 'HMD': ['Heard Island and McDonald Islands'],
 'HND': ['Honduras'],
 'HRV': ['Croatia'],
 'HTI': ['Haiti'],
 'HUN': ['Hungary'],
 'IDN': ['Indonesia'],
 'IMN': ['Isle of Man'],
 'IND': ['India'],
 'IOT': ['British Indian Ocean Territory'],
 'IRL': ['Ireland'],
 'IRN': ['Iran'],
 'IRQ': ['Iraq'],
 'ISL': ['Iceland'],
 'ISR': ['Israel'],
 'ITA': ['Italy'],
 'JAM': ['Jamaica'],
 'JEY': ['Jersey'],
 'JOR': ['Jordan'],
 'JPN': ['Japan'],
 'KAZ': ['Kazakhstan'],
 'KEN': ['Kenya'],
 'KGZ': ['Kyrgyzstan','Kyrgyz'],
 'KHM': ['Cambodia'],
 'KIR': ['Kiribati'],
 'KNA': ['St. Kitts & Nevis','St. Kitts and Nevis','Saint Christopher and Nevis'],
 'KOR': ['South Korea','Republic of Korea'],
 'KWT': ['Kuwait'],
 'LAO': ['Laos'],
 'LBN': ['Lebanon'],
 'LBR': ['Liberia'],
 'LBY': ['Libya'],
 'LCA': ['St. Lucia'],
 'LIE': ['Liechtenstein'],
 'LKA': ['Sri Lanka'],
 'LSO': ['Lesotho'],
 'LTU': ['Lithuania'],
 'LUX': ['Luxembourg'],
 'LVA': ['Latvia'],
 'MAC': ['Macao'],
 'MAF': ['Saint Martin (France)'],
 'MAR': ['Morocco'],
 'MCO': ['Monaco'],
 'MDA': ['Moldova'],
 'MDG': ['Madagascar'],
 'MDV': ['Maldives'],
 'MEX': ['Mexico'],
 'MHL': ['Marshall islands'],
 'MKD': ['Republic of Macedonia','North Macedonia'],
 'MLI': ['Mali'],
 'MLT': ['Malta'],
 'MMR': ['Myanmar','Burma'],
 'MNE': ['Montenegro'],
 'MNG': ['Mongolia'],
 'MNP': ['Northern Mariana Islands'],
 'MOZ': ['Mozambique'],
 'MRT': ['Mauritania'],
 'MSR': ['Montserrat'],
 'MTQ': ['Martinique'],
 'MUS': ['Mauritius'],
 'MWI': ['Malawi'],
 'MYS': ['Malaysia'],
 'MYT': ['Mayotte'],
 'NAM': ['Namibia'],
 'NCL': ['New Caledonia'],
 'NER': ['Niger'],
 'NFK': ['Norfolk Island'],
 'NGA': ['Nigeria'],
 'NIC': ['Nicaragua'],
 'NIU': ['Niue'],
 'NLD': ['Netherlands'],
 'NOR': ['Norway'],
 'NPL': ['Nepal'],
 'NRU': ['Nauru'],
 'NZL': ['New Zealand'],
 'OMN': ['Oman'],
 'PAK': ['Pakistan'],
 'PAN': ['Panama'],
 'PCN': ['Pitcairn Islands'],
 'PER': ['Peru'],
 'PHL': ['The Philippines','Philippines'],
 'PLW': ['Palau'],
 'PNG': ['Papua New Guinea'],
 'POL': ['Poland'],
 'PRI': ['Puerto Rico'],
 'PRK': ['North Korea'],
 'PRT': ['Portugal'],
 'PRY': ['Paraguay'],
 'PSE': ['Palestinian territories'],
 'PYF': ['French polynesia'],
 'QAT': ['Qatar'],
 'REU': ['Réunion'],
 'ROU': ['Romania'],
 'RUS': ['Russian Federation','Russia'],
 'RWA': ['Rwanda'],
 'SAU': ['Saudi Arabia'],
 'SDN': ['Sudan'],
 'SEN': ['Senegal'],
 'SGP': ['Singapore'],
 'SGS': ['South Georgia and the South Sandwich Islands'],
 'SHN': ['St. Helena & Dependencies','St. Helena and Dependencies'],
 'SJM': ['Template:Country data SJM Svalbard'],
 'SLB': ['Solomon Islands'],
 'SLE': ['Sierra Leone'],
 'SLV': ['El Salvador'],
 'SMR': ['San Marino'],
 'SOM': ['Somalia'],
 'SPM': ['Saint-Pierre and Miquelon'],
 'SRB': ['Serbia'],
 'SSD': ['South Sudan'],
 'STP': ['Sao Tome & Principe','Sao Tome and Principe'],
 'SUR': ['Suriname'],
 'SVK': ['Slovakia'],
 'SVN': ['Slovenia'],
 'SWE': ['Sweden'],
 'SWZ': ['Swaziland','Eswatini'],
 'SYC': ['Seychelles'],
 'SYR': ['Syria'],
 'TCA': ['Turks & Caicos Islands','Turks and Caicos Islands'],
 'TCD': ['Chad'],
 'TGO': ['Togo'],
 'THA': ['Thailand'],
 'TJK': ['Tajikistan'],
 'TKL': ['Tokelau'],
 'TKM': ['Turkmenistan'],
 'TLS': ['Timor-Leste (East Timor)'],
 'TON': ['Tonga'],
 'TTO': ['Trinidad & Tobago','Trinidad and Tobago'],
 'TUN': ['Tunisia'],
 'TUR': ['Turkey'],
 'TUV': ['Tuvalu'],
 'TWN': ['Taiwan'],
 'TZA': ['Tanzania'],
 'UGA': ['Uganda'],
 'UKR': ['Ukraine'],
 'UMI': ['United States Minor Outlying Islands'],
 'URY': ['Uruguay'],
 'USA': ['United States of America','USA'],
 'UZB': ['Uzbekistan'],
 'VAT': ['Vatican City','Vatican'],
 'VCT': ['St. Vincent & the Grenadines','St. Vincent and the Grenadines','Saint Vincent and the Grenadines'],
 'VEN': ['Venezuela'],
 'VGB': ['British Virgin Islands'],
 'VIR': ['United States Virgin Islands'],
 'VNM': ['Vietnam','Viet Nam'],
 'VUT': ['Vanuatu'],
 'WLF': ['Wallis and Futuna'],
 'WSM': ['Samoa'],
 'YEM': ['Yemen'],
 'ZAF': ['South Africa'],
 'ZMB': ['Zambia'],
 'ZWE': ['Zimbabwe']
 }

for code, names in COUNTRY_ISO.items():
    for name in names:
        COUNTRY_DICT[name] = code
def get_country_code(country_name):
    if country_name in COUNTRY_DICT:
       return COUNTRY_DICT[country_name]
    else:
        return country_name + " : NOT FOUND"

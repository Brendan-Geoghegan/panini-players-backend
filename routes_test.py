import json

def test_get_individual_sticker(api):
    """BRA1 sticker code returns object with sticker data"""
    resp = api.get('/stickers/BRA1')
    assert resp.status == '200 OK'
    assert b'{\n  "code": "BRA1",\n  "image": "cdn.shopify.com/s/files/1/0561/4639/5336/products/IMG_2252@2x.jpg",\n  "name": "Brazil Team",\n  "price": "\\u00a30.29"\n}\n' in resp.data


def test_get_user(api):
    """User ID returns user data"""
    resp = api.get(
        '/users/Sean')  # User ID will need to be updated when database is reinitialised
    assert resp.status == '200 OK'
    assert b'[\n  {\n    \"cards\": \"00-0 FWC1-0 FWC2-0 FWC3-0 FWC4-0 FWC5-0 FWC6-0 FWC7-0 FWC8-0 FWC9-0 FWC10-0 FWC11-0 FWC12-0 FWC13-0 FWC14-0 FWC15-0 FWC16-0 FWC17-0 FWC18-0 FWC19-0 FWC20-0 FWC21-0 FWC22-0 FWC23-0 FWC24-0 FWC25-0 FWC26-0 FWC27-0 FWC28-0 FWC29-0 QAT1-0 QAT2-0 QAT3-0 QAT4-0 QAT5-0 QAT6-0 QAT7-0 QAT8-0 QAT9-0 QAT10-0 QAT11-0 QAT12-0 QAT13-0 QAT14-0 QAT15-0 QAT16-0 QAT17-0 QAT18-0 QAT19-0 QAT20-0 ECU1-1 ECU2-0 ECU3-0 ECU4-0 ECU5-0 ECU6-0 ECU7-0 ECU8-0 ECU9-0 ECU10-0 ECU11-0 ECU12-0 ECU13-0 ECU14-0 ECU15-0 ECU16-0 ECU17-0 ECU18-0 ECU19-0 ECU20-0 SEN1-0 SEN2-0 SEN3-0 SEN4-0 SEN5-0 SEN6-0 SEN7-0 SEN8-0 SEN9-0 SEN10-0 SEN11-0 SEN12-0 SEN13-0 SEN14-0 SEN15-0 SEN16-0 SEN17-0 SEN18-0 SEN19-0 SEN20-0 NED1-0 NED2-0 NED3-0 NED4-0 NED5-0 NED6-0 NED7-0 NED8-0 NED9-0 NED10-0 NED11-0 NED12-0 NED13-0 NED14-0 NED15-0 NED16-0 NED17-0 NED18-0 NED19-0 NED20-0 ENG1-0 ENG2-0 ENG3-0 ENG4-0 ENG5-0 ENG6-0 ENG7-0 ENG8-0 ENG9-0 ENG10-0 ENG11-0 ENG12-0 ENG13-0 ENG14-0 ENG15-0 ENG16-0 ENG17-0 ENG18-0 ENG19-0 ENG20-0 IRN1-0 IRN2-0 IRN3-0 IRN4-0 IRN5-0 IRN6-0 IRN7-0 IRN8-0 IRN9-0 IRN10-0 IRN11-0 IRN12-0 IRN13-0 IRN14-0 IRN15-0 IRN16-0 IRN17-0 IRN18-0 IRN19-0 IRN20-0 USA1-0 USA2-0 USA3-0 USA4-0 USA5-0 USA6-0 USA7-0 USA8-0 USA9-0 USA10-0 USA11-0 USA12-0 USA13-0 USA14-0 USA15-0 USA16-0 USA17-0 USA18-0 USA19-0 USA20-0 WAL1-0 WAL2-0 WAL3-0 WAL4-0 WAL5-0 WAL6-0 WAL7-0 WAL8-0 WAL9-0 WAL10-0 WAL11-0 WAL12-0 WAL13-0 WAL14-0 WAL15-0 WAL16-0 WAL17-0 WAL18-0 WAL19-0 WAL20-0 ARG1-0 ARG2-0 ARG3-0 ARG4-0 ARG5-0 ARG6-0 ARG7-0 ARG8-0 ARG9-0 ARG10-0 ARG11-0 ARG12-0 ARG13-0 ARG14-0 ARG15-0 ARG16-0 ARG17-0 ARG18-0 ARG19-0 ARG20-0 KSA1-0 KSA2-0 KSA3-0 KSA4-0 KSA5-0 KSA5-0 KSA7-0 KSA8-0 KSA9-0 KSA10-0 KSA11-0 KSA12-0 KSA13-0 KSA14-0 KSA15-0 KSA16-0 KSA17-0 KSA18-0 KSA19-0 KSA20-0 MEX1-0 MEX2-0 MEX3-0 MEX4-0 MEX5-0 MEX6-0 MEX7-0 MEX8-0 MEX9-0 MEX10-0 MEX11-0 MEX12-0 MEX13-0 MEX14-0 MEX15-0 MEX16-0 MEX17-0 MEX18-0 MEX19-0 MEX20-0 POL1-0 POL2-0 POL3-0 POL4-0 POL5-0 POL6-0 POL7-0 POL8-0 POL9-0 POL10-0 POL11-0 POL12-0 POL13-0 POL14-0 POL15-0 POL16-0 POL17-0 POL18-0 POL19-0 POL20-0 FRA1-0 FRA2-0 FRA3-0 FRA4-0 FRA5-0 FRA6-0 FRA7-0 FRA8-0 FRA9-0 FRA10-0 FRA11-0 FRA12-0 FRA13-0 FRA14-0 FRA15-0 FRA16-0 FRA17-0 FRA18-0 FRA19-0 FRA20-0 AUS1-0 AUS2-0 AUS3-0 AUS4-0 AUS5-0 AUS6-0 AUS7-0 AUS8-0 AUS9-0 AUS10-0 AUS11-0 AUS12-0 AUS13-0 AUS14-0 AUS15-0 AUS16-0 AUS17-0 AUS18-0 AUS19-0 AUS20-0 DEN1-0 DEN2-0 DEN3-0 DEN4-0 DEN5-0 DEN6-0 DEN7-0 DEN8-0 DEN9-0 DEN10-0 DEN11-0 DEN12-0 DEN13-0 DEN14-0 DEN15-0 DEN16-0 DEN17-0 DEN18-0 DEN19-0 DEN20-0 TUN1-0 TUN2-0 TUN3-0 TUN4-0 TUN5-0 TUN6-0 TUN7-0 TUN8-0 TUN9-0 TUN10-0 TUN11-0 TUN12-0 TUN13-0 TUN14-0 TUN15-0 TUN16-0 TUN17-0 TUN18-0 TUN19-0 TUN20-0 ESP1-0 ESP2-0 ESP3-0 ESP4-0 ESP5-0 ESP6-0 ESP7-0 ESP8-0 ESP9-0 ESP10-0 ESP11-0 ESP12-0 ESP13-0 ESP14-0 ESP15-0 ESP16-0 ESP17-0 ESP18-0 ESP19-0 ESP20-0 CRC1-0 CRC2-0 CRC3-0 CRC4-0 CRC5-0 CRC6-0 CRC7-0 CRC8-0 CRC9-0 CRC10-0 CRC11-0 CRC12-0 CRC13-0 CRC14-0 CRC15-0 CRC16-0 CRC17-0 CRC18-0 CRC19-0 CRC20-0 GER1-0 GER2-0 GER3-0 GER4-0 GER5-0 GER6-0 GER7-0 GER8-0 GER9-0 GER10-0 GER11-0 GER12-0 GER13-0 GER14-0 GER15-0 GER16-0 GER17-0 GER18-0 GER19-0 GER20-0 JPN1-0 JPN2-0 JPN3-0 JPN4-0 JPN5-0 JPN6-0 JPN7-0 JPN8-0 JPN9-0 JPN10-0 JPN11-0 JPN12-0 JPN13-0 JPN14-0 JPN15-0 JPN16-0 JPN17-0 JPN18-0 JPN19-0 JPN20-0 BEL1-0 BEL2-0 BEL3-0 BEL4-0 BEL5-0 BEL6-0 BEL7-0 BEL8-0 BEL9-0 BEL10-0 BEL11-0 BEL12-0 BEL13-0 BEL14-0 BEL15-0 BEL16-0 BEL17-0 BEL18-0 BEL19-0 BEL20-0 CAN1-0 CAN2-0 CAN3-0 CAN4-0 CAN5-0 CAN6-0 CAN7-0 CAN8-0 CAN9-0 CAN10-0 CAN11-0 CAN12-0 CAN13-0 CAN14-0 CAN15-0 CAN16-0 CAN17-0 CAN18-0 CAN19-0 CAN20-0 MAR1-0 MAR2-0 MAR3-0 MAR4-0 MAR5-0 MAR6-0 MAR7-0 MAR8-0 MAR9-0 MAR10-0 MAR11-0 MAR12-0 MAR13-0 MAR14-0 MAR15-0 MAR16-0 MAR17-0 MAR18-0 MAR19-0 MAR20-0 CRO1-0 CRO2-0 CRO3-0 CRO4-0 CRO5-0 CRO6-0 CRO7-0 CRO8-0 CRO9-0 CRO10-0 CRO11-0 CRO12-0 CRO13-0 CRO14-0 CRO15-0 CRO16-0 CRO17-0 CRO18-0 CRO19-0 CRO20-0 BRA1-0 BRA2-0 BRA3-0 BRA4-0 BRA5-0 BRA6-0 BRA7-0 BRA8-0 BRA9-0 BRA10-0 BRA11-0 BRA12-0 BRA13-0 BRA14-0 BRA15-0 BRA16-0 BRA17-0 BRA18-0 BRA19-0 BRA20-0 SRB1-0 SRB2-0 SRB3-0 SRB4-0 SRB5-0 SRB6-0 SRB7-0 SRB8-0 SRB9-0 SRB10-0 SRB11-0 SRB12-0 SRB13-0 SRB14-0 SRB15-0 SRB16-0 SRB17-0 SRB18-0 SRB19-0 SRB20-0 SUI1-0 SUI2-0 SUI3-0 SUI4-0 SUI5-0 SUI6-0 SUI7-0 SUI8-0 SUI9-0 SUI10-0 SUI11-0 SUI12-0 SUI13-0 SUI14-0 SUI15-0 SUI16-0 SUI17-0 SUI18-0 SUI19-0 SUI20-0 CMR1-0 CMR2-0 CMR3-0 CMR4-0 CMR5-0 CMR6-0 CMR7-0 CMR8-0 CMR9-0 CMR10-0 CMR11-0 CMR12-0 CMR13-0 CMR14-0 CMR15-0 CMR16-0 CMR17-0 CMR18-0 CMR19-0 CMR20-0 POR1-0 POR2-0 POR3-0 POR4-0 POR5-0 POR6-0 POR7-0 POR8-0 POR9-0 POR10-0 POR11-0 POR12-0 POR13-0 POR14-0 POR15-0 POR16-0 POR17-0 POR18-0 POR19-0 POR20-0 GHA1-0 GHA2-0 GHA3-0 GHA4-0 GHA5-0 GHA6-0 GHA7-0 GHA8-0 GHA9-0 GHA10-0 GHA11-0 GHA12-0 GHA13-0 GHA14-0 GHA15-0 GHA16-0 GHA17-0 GHA18-0 GHA19-0 GHA20-0 URU1-0 URU2-0 URU3-0 URU4-0 URU5-0 URU6-0 URU7-0 URU8-0 URU9-0 URU10-0 URU11-0 URU12-0 URU13-0 URU14-0 URU15-0 URU16-0 URU17-0 URU18-0 URU19-0 URU20-0 KOR1-0 KOR2-0 KOR3-0 KOR4-0 KOR5-0 KOR6-0 KOR7-0 KOR8-0 KOR9-0 KOR10-0 KOR11-0 KOR12-0 KOR13-0 KOR14-0 KOR15-0 KOR16-0 KOR17-0 KOR18-0 KOR19-0 KOR20-0\",\n    \"email\": \"sean@123.com\",\n    \"friends\": \"\",\n    \"id\": \"89il2j3i9c\",\n    \"location\": \"London\",\n    \"password\": \"password123\",\n    \"username\": \"Sean\"\n  },\n  200\n]' in resp.data


def test_get_country_stickers(api):
    """Country code BRA returns all stickers for Brazil team"""
    resp = api.get('/country/BRA')
    assert resp.status == '200 OK'
    assert b'[\n  {\n    \"code\": \"BRA1\",\n    \"image\": \"cdn.shopify.com/s/files/1/0561/4639/5336/products/IMG_2252@2x.jpg\",\n    \"name\": \"Brazil Team\",\n    \"price\": \"\\u00a30.29\"\n  },\n  {\n    \"code\": \"BRA2\",\n    \"image\": \"cdn.shopify.com/s/files/1/0561/4639/5336/products/IMG_2253@2x.jpg\",\n    \"name\": \"Brazil Logo\",\n    \"price\": \"\\u00a30.59\"\n  },\n  {\n    \"code\": \"BRA3\",\n    \"image\": \"cdn.shopify.com/s/files/1/0561/4639/5336/products/IMG_2448_8e1a95cd-3c13-4ad1-be51-8a2bd043e65f@2x.jpg\",\n    \"name\": \"Alisson\",\n    \"price\": \"\\u00a30.29\"\n  },\n  {\n    \"code\": \"BRA4\",\n    \"image\": \"cdn.shopify.com/s/files/1/0561/4639/5336/products/IMG_2254@2x.jpg\",\n    \"name\": \"Ederson\",\n    \"price\": \"\\u00a30.29\"\n  },\n  {\n    \"code\": \"BRA5\",\n    \"image\": \"cdn.shopify.com/s/files/1/0561/4639/5336/products/IMG_2449_00f7b0ea-e9bb-46d4-83ba-71b3583bae1d@2x.jpg\",\n    \"name\": \"Alex Sandro\",\n    \"price\": \"\\u00a30.29\"\n  },\n  {\n    \"code\": \"BRA6\",\n    \"image\": \"cdn.shopify.com/s/files/1/0561/4639/5336/products/IMG_2255@2x.jpg\",\n    \"name\": \"Danilo\",\n    \"price\": \"\\u00a30.29\"\n  },\n  {\n    \"code\": \"BRA7\",\n    \"image\": \"cdn.shopify.com/s/files/1/0561/4639/5336/products/IMG_2256@2x.jpg\",\n    \"name\": \"\\u00c9der Militao\",\n    \"price\": \"\\u00a30.29\"\n  },\n  {\n    \"code\": \"BRA8\",\n    \"image\": \"cdn.shopify.com/s/files/1/0561/4639/5336/products/IMG_2257@2x.jpg\",\n    \"name\": \"Marquinhos\",\n    \"price\": \"\\u00a30.29\"\n  },\n  {\n    \"code\": \"BRA9\",\n    \"image\": \"cdn.shopify.com/s/files/1/0561/4639/5336/products/IMG_2258@2x.jpg\",\n    \"name\": \"Thiago Silva\",\n    \"price\": \"\\u00a30.29\"\n  },\n  {\n    \"code\": \"BRA10\",\n    \"image\": \"cdn.shopify.com/s/files/1/0561/4639/5336/products/IMG_2259@2x.jpg\",\n    \"name\": \"Casemiro\",\n    \"price\": \"\\u00a30.29\"\n  },\n  {\n    \"code\": \"BRA11\",\n    \"image\": \"cdn.shopify.com/s/files/1/0561/4639/5336/products/IMG_2260@2x.jpg\",\n    \"name\": \"Philippe Coutinho\",\n    \"price\": \"\\u00a30.29\"\n  },\n  {\n    \"code\": \"BRA12\",\n    \"image\": \"cdn.shopify.com/s/files/1/0561/4639/5336/products/IMG_2261_70a3c06a-652f-4045-8ea9-07fbbcc32a6b@2x.jpg\",\n    \"name\": \"Fabinho\",\n    \"price\": \"\\u00a30.29\"\n  },\n  {\n    \"code\": \"BRA13\",\n    \"image\": \"cdn.shopify.com/s/files/1/0561/4639/5336/products/IMG_2262@2x.jpg\",\n    \"name\": \"Fred\",\n    \"price\": \"\\u00a30.29\"\n  },\n  {\n    \"code\": \"BRA14\",\n    \"image\": \"cdn.shopify.com/s/files/1/0561/4639/5336/products/IMG_2263@2x.jpg\",\n    \"name\": \"Lucas Paquet\\u00e1\",\n    \"price\": \"\\u00a30.29\"\n  },\n  {\n    \"code\": \"BRA15\",\n    \"image\": \"cdn.shopify.com/s/files/1/0561/4639/5336/products/IMG_2264@2x.jpg\",\n    \"name\": \"Antony\",\n    \"price\": \"\\u00a30.29\"\n  },\n  {\n    \"code\": \"BRA16\",\n    \"image\": \"cdn.shopify.com/s/files/1/0561/4639/5336/products/IMG_2265@2x.jpg\",\n    \"name\": \"Gabriel Jesus\",\n    \"price\": \"\\u00a30.29\"\n  },\n  {\n    \"code\": \"BRA17\",\n    \"image\": \"cdn.shopify.com/s/files/1/0561/4639/5336/products/IMG_2266@2x.jpg\",\n    \"name\": \"Neymar JR\",\n    \"price\": \"\\u00a30.29\"\n  },\n  {\n    \"code\": \"BRA18\",\n    \"image\": \"cdn.shopify.com/s/files/1/0561/4639/5336/products/IMG_2267@2x.jpg\",\n    \"name\": \"Raphinha\",\n    \"price\": \"\\u00a30.29\"\n  },\n  {\n    \"code\": \"BRA19\",\n    \"image\": \"cdn.shopify.com/s/files/1/0561/4639/5336/products/IMG_2268_0e9019ec-24b2-4efc-a264-291cdd9027b3@2x.jpg\",\n    \"name\": \"Richarlison\",\n    \"price\": \"\\u00a30.29\"\n  },\n  {\n    \"code\": \"BRA20\",\n    \"image\": \"cdn.shopify.com/s/files/1/0561/4639/5336/products/IMG_2269_9ba4bd61-ae39-4a45-90a1-e46ff9e09886@2x.jpg\",\n    \"name\": \"Vin\\u00edcius JR\",\n    \"price\": \"\\u00a30.29\"\n  }\n]' in resp.data


def test_get_user_friends(api):
    """User ID returns user's friends as string"""
    resp = api.get('/friends/89il2j3i9c')
    assert resp.status == '200 OK'
    assert b'' in resp.data


# def test_add_friend(api):
#     pass


def test_get_friends_list(api):
    """User ID returns user's friends as a list of strings"""
    resp = api.get('/users/89il2j3i9c/friends')
    assert resp.status == '200 OK'
    assert b'' in resp.data


def test_get_users_stickers(api):
    """User ID gets all stickers in user's collection"""
    resp = api.get('/users/89il2j3i9c/stickers')
    assert resp.status == '200 OK'
    assert b'{\n  \"00\": 0,\n  \"ARG1\": 0,\n  \"ARG10\": 0,\n  \"ARG11\": 0,\n  \"ARG12\": 0,\n  \"ARG13\": 0,\n  \"ARG14\": 0,\n  \"ARG15\": 0,\n  \"ARG16\": 0,\n  \"ARG17\": 0,\n  \"ARG18\": 0,\n  \"ARG19\": 0,\n  \"ARG2\": 0,\n  \"ARG20\": 0,\n  \"ARG3\": 0,\n  \"ARG4\": 0,\n  \"ARG5\": 0,\n  \"ARG6\": 0,\n  \"ARG7\": 0,\n  \"ARG8\": 0,\n  \"ARG9\": 0,\n  \"AUS1\": 0,\n  \"AUS10\": 0,\n  \"AUS11\": 0,\n  \"AUS12\": 0,\n  \"AUS13\": 0,\n  \"AUS14\": 0,\n  \"AUS15\": 0,\n  \"AUS16\": 0,\n  \"AUS17\": 0,\n  \"AUS18\": 0,\n  \"AUS19\": 0,\n  \"AUS2\": 0,\n  \"AUS20\": 0,\n  \"AUS3\": 0,\n  \"AUS4\": 0,\n  \"AUS5\": 0,\n  \"AUS6\": 0,\n  \"AUS7\": 0,\n  \"AUS8\": 0,\n  \"AUS9\": 0,\n  \"BEL1\": 0,\n  \"BEL10\": 0,\n  \"BEL11\": 0,\n  \"BEL12\": 0,\n  \"BEL13\": 0,\n  \"BEL14\": 0,\n  \"BEL15\": 0,\n  \"BEL16\": 0,\n  \"BEL17\": 0,\n  \"BEL18\": 0,\n  \"BEL19\": 0,\n  \"BEL2\": 0,\n  \"BEL20\": 0,\n  \"BEL3\": 0,\n  \"BEL4\": 0,\n  \"BEL5\": 0,\n  \"BEL6\": 0,\n  \"BEL7\": 0,\n  \"BEL8\": 0,\n  \"BEL9\": 0,\n  \"BRA1\": 0,\n  \"BRA10\": 0,\n  \"BRA11\": 0,\n  \"BRA12\": 0,\n  \"BRA13\": 0,\n  \"BRA14\": 0,\n  \"BRA15\": 0,\n  \"BRA16\": 0,\n  \"BRA17\": 0,\n  \"BRA18\": 0,\n  \"BRA19\": 0,\n  \"BRA2\": 0,\n  \"BRA20\": 0,\n  \"BRA3\": 0,\n  \"BRA4\": 0,\n  \"BRA5\": 0,\n  \"BRA6\": 0,\n  \"BRA7\": 0,\n  \"BRA8\": 0,\n  \"BRA9\": 0,\n  \"CAN1\": 0,\n  \"CAN10\": 0,\n  \"CAN11\": 0,\n  \"CAN12\": 0,\n  \"CAN13\": 0,\n  \"CAN14\": 0,\n  \"CAN15\": 0,\n  \"CAN16\": 0,\n  \"CAN17\": 0,\n  \"CAN18\": 0,\n  \"CAN19\": 0,\n  \"CAN2\": 0,\n  \"CAN20\": 0,\n  \"CAN3\": 0,\n  \"CAN4\": 0,\n  \"CAN5\": 0,\n  \"CAN6\": 0,\n  \"CAN7\": 0,\n  \"CAN8\": 0,\n  \"CAN9\": 0,\n  \"CMR1\": 0,\n  \"CMR10\": 0,\n  \"CMR11\": 0,\n  \"CMR12\": 0,\n  \"CMR13\": 0,\n  \"CMR14\": 0,\n  \"CMR15\": 0,\n  \"CMR16\": 0,\n  \"CMR17\": 0,\n  \"CMR18\": 0,\n  \"CMR19\": 0,\n  \"CMR2\": 0,\n  \"CMR20\": 0,\n  \"CMR3\": 0,\n  \"CMR4\": 0,\n  \"CMR5\": 0,\n  \"CMR6\": 0,\n  \"CMR7\": 0,\n  \"CMR8\": 0,\n  \"CMR9\": 0,\n  \"CRC1\": 0,\n  \"CRC10\": 0,\n  \"CRC11\": 0,\n  \"CRC12\": 0,\n  \"CRC13\": 0,\n  \"CRC14\": 0,\n  \"CRC15\": 0,\n  \"CRC16\": 0,\n  \"CRC17\": 0,\n  \"CRC18\": 0,\n  \"CRC19\": 0,\n  \"CRC2\": 0,\n  \"CRC20\": 0,\n  \"CRC3\": 0,\n  \"CRC4\": 0,\n  \"CRC5\": 0,\n  \"CRC6\": 0,\n  \"CRC7\": 0,\n  \"CRC8\": 0,\n  \"CRC9\": 0,\n  \"CRO1\": 0,\n  \"CRO10\": 0,\n  \"CRO11\": 0,\n  \"CRO12\": 0,\n  \"CRO13\": 0,\n  \"CRO14\": 0,\n  \"CRO15\": 0,\n  \"CRO16\": 0,\n  \"CRO17\": 0,\n  \"CRO18\": 0,\n  \"CRO19\": 0,\n  \"CRO2\": 0,\n  \"CRO20\": 0,\n  \"CRO3\": 0,\n  \"CRO4\": 0,\n  \"CRO5\": 0,\n  \"CRO6\": 0,\n  \"CRO7\": 0,\n  \"CRO8\": 0,\n  \"CRO9\": 0,\n  \"DEN1\": 0,\n  \"DEN10\": 0,\n  \"DEN11\": 0,\n  \"DEN12\": 0,\n  \"DEN13\": 0,\n  \"DEN14\": 0,\n  \"DEN15\": 0,\n  \"DEN16\": 0,\n  \"DEN17\": 0,\n  \"DEN18\": 0,\n  \"DEN19\": 0,\n  \"DEN2\": 0,\n  \"DEN20\": 0,\n  \"DEN3\": 0,\n  \"DEN4\": 0,\n  \"DEN5\": 0,\n  \"DEN6\": 0,\n  \"DEN7\": 0,\n  \"DEN8\": 0,\n  \"DEN9\": 0,\n  \"ECU1\": 1,\n  \"ECU10\": 0,\n  \"ECU11\": 0,\n  \"ECU12\": 0,\n  \"ECU13\": 0,\n  \"ECU14\": 0,\n  \"ECU15\": 0,\n  \"ECU16\": 0,\n  \"ECU17\": 0,\n  \"ECU18\": 0,\n  \"ECU19\": 0,\n  \"ECU2\": 0,\n  \"ECU20\": 0,\n  \"ECU3\": 0,\n  \"ECU4\": 0,\n  \"ECU5\": 0,\n  \"ECU6\": 0,\n  \"ECU7\": 0,\n  \"ECU8\": 0,\n  \"ECU9\": 0,\n  \"ENG1\": 0,\n  \"ENG10\": 0,\n  \"ENG11\": 0,\n  \"ENG12\": 0,\n  \"ENG13\": 0,\n  \"ENG14\": 0,\n  \"ENG15\": 0,\n  \"ENG16\": 0,\n  \"ENG17\": 0,\n  \"ENG18\": 0,\n  \"ENG19\": 0,\n  \"ENG2\": 0,\n  \"ENG20\": 0,\n  \"ENG3\": 0,\n  \"ENG4\": 0,\n  \"ENG5\": 0,\n  \"ENG6\": 0,\n  \"ENG7\": 0,\n  \"ENG8\": 0,\n  \"ENG9\": 0,\n  \"ESP1\": 0,\n  \"ESP10\": 0,\n  \"ESP11\": 0,\n  \"ESP12\": 0,\n  \"ESP13\": 0,\n  \"ESP14\": 0,\n  \"ESP15\": 0,\n  \"ESP16\": 0,\n  \"ESP17\": 0,\n  \"ESP18\": 0,\n  \"ESP19\": 0,\n  \"ESP2\": 0,\n  \"ESP20\": 0,\n  \"ESP3\": 0,\n  \"ESP4\": 0,\n  \"ESP5\": 0,\n  \"ESP6\": 0,\n  \"ESP7\": 0,\n  \"ESP8\": 0,\n  \"ESP9\": 0,\n  \"FRA1\": 0,\n  \"FRA10\": 0,\n  \"FRA11\": 0,\n  \"FRA12\": 0,\n  \"FRA13\": 0,\n  \"FRA14\": 0,\n  \"FRA15\": 0,\n  \"FRA16\": 0,\n  \"FRA17\": 0,\n  \"FRA18\": 0,\n  \"FRA19\": 0,\n  \"FRA2\": 0,\n  \"FRA20\": 0,\n  \"FRA3\": 0,\n  \"FRA4\": 0,\n  \"FRA5\": 0,\n  \"FRA6\": 0,\n  \"FRA7\": 0,\n  \"FRA8\": 0,\n  \"FRA9\": 0,\n  \"FWC1\": 0,\n  \"FWC10\": 0,\n  \"FWC11\": 0,\n  \"FWC12\": 0,\n  \"FWC13\": 0,\n  \"FWC14\": 0,\n  \"FWC15\": 0,\n  \"FWC16\": 0,\n  \"FWC17\": 0,\n  \"FWC18\": 0,\n  \"FWC19\": 0,\n  \"FWC2\": 0,\n  \"FWC20\": 0,\n  \"FWC21\": 0,\n  \"FWC22\": 0,\n  \"FWC23\": 0,\n  \"FWC24\": 0,\n  \"FWC25\": 0,\n  \"FWC26\": 0,\n  \"FWC27\": 0,\n  \"FWC28\": 0,\n  \"FWC29\": 0,\n  \"FWC3\": 0,\n  \"FWC4\": 0,\n  \"FWC5\": 0,\n  \"FWC6\": 0,\n  \"FWC7\": 0,\n  \"FWC8\": 0,\n  \"FWC9\": 0,\n  \"GER1\": 0,\n  \"GER10\": 0,\n  \"GER11\": 0,\n  \"GER12\": 0,\n  \"GER13\": 0,\n  \"GER14\": 0,\n  \"GER15\": 0,\n  \"GER16\": 0,\n  \"GER17\": 0,\n  \"GER18\": 0,\n  \"GER19\": 0,\n  \"GER2\": 0,\n  \"GER20\": 0,\n  \"GER3\": 0,\n  \"GER4\": 0,\n  \"GER5\": 0,\n  \"GER6\": 0,\n  \"GER7\": 0,\n  \"GER8\": 0,\n  \"GER9\": 0,\n  \"GHA1\": 0,\n  \"GHA10\": 0,\n  \"GHA11\": 0,\n  \"GHA12\": 0,\n  \"GHA13\": 0,\n  \"GHA14\": 0,\n  \"GHA15\": 0,\n  \"GHA16\": 0,\n  \"GHA17\": 0,\n  \"GHA18\": 0,\n  \"GHA19\": 0,\n  \"GHA2\": 0,\n  \"GHA20\": 0,\n  \"GHA3\": 0,\n  \"GHA4\": 0,\n  \"GHA5\": 0,\n  \"GHA6\": 0,\n  \"GHA7\": 0,\n  \"GHA8\": 0,\n  \"GHA9\": 0,\n  \"IRN1\": 0,\n  \"IRN10\": 0,\n  \"IRN11\": 0,\n  \"IRN12\": 0,\n  \"IRN13\": 0,\n  \"IRN14\": 0,\n  \"IRN15\": 0,\n  \"IRN16\": 0,\n  \"IRN17\": 0,\n  \"IRN18\": 0,\n  \"IRN19\": 0,\n  \"IRN2\": 0,\n  \"IRN20\": 0,\n  \"IRN3\": 0,\n  \"IRN4\": 0,\n  \"IRN5\": 0,\n  \"IRN6\": 0,\n  \"IRN7\": 0,\n  \"IRN8\": 0,\n  \"IRN9\": 0,\n  \"JPN1\": 0,\n  \"JPN10\": 0,\n  \"JPN11\": 0,\n  \"JPN12\": 0,\n  \"JPN13\": 0,\n  \"JPN14\": 0,\n  \"JPN15\": 0,\n  \"JPN16\": 0,\n  \"JPN17\": 0,\n  \"JPN18\": 0,\n  \"JPN19\": 0,\n  \"JPN2\": 0,\n  \"JPN20\": 0,\n  \"JPN3\": 0,\n  \"JPN4\": 0,\n  \"JPN5\": 0,\n  \"JPN6\": 0,\n  \"JPN7\": 0,\n  \"JPN8\": 0,\n  \"JPN9\": 0,\n  \"KOR1\": 0,\n  \"KOR10\": 0,\n  \"KOR11\": 0,\n  \"KOR12\": 0,\n  \"KOR13\": 0,\n  \"KOR14\": 0,\n  \"KOR15\": 0,\n  \"KOR16\": 0,\n  \"KOR17\": 0,\n  \"KOR18\": 0,\n  \"KOR19\": 0,\n  \"KOR2\": 0,\n  \"KOR20\": 0,\n  \"KOR3\": 0,\n  \"KOR4\": 0,\n  \"KOR5\": 0,\n  \"KOR6\": 0,\n  \"KOR7\": 0,\n  \"KOR8\": 0,\n  \"KOR9\": 0,\n  \"KSA1\": 0,\n  \"KSA10\": 0,\n  \"KSA11\": 0,\n  \"KSA12\": 0,\n  \"KSA13\": 0,\n  \"KSA14\": 0,\n  \"KSA15\": 0,\n  \"KSA16\": 0,\n  \"KSA17\": 0,\n  \"KSA18\": 0,\n  \"KSA19\": 0,\n  \"KSA2\": 0,\n  \"KSA20\": 0,\n  \"KSA3\": 0,\n  \"KSA4\": 0,\n  \"KSA5\": 0,\n  \"KSA7\": 0,\n  \"KSA8\": 0,\n  \"KSA9\": 0,\n  \"MAR1\": 0,\n  \"MAR10\": 0,\n  \"MAR11\": 0,\n  \"MAR12\": 0,\n  \"MAR13\": 0,\n  \"MAR14\": 0,\n  \"MAR15\": 0,\n  \"MAR16\": 0,\n  \"MAR17\": 0,\n  \"MAR18\": 0,\n  \"MAR19\": 0,\n  \"MAR2\": 0,\n  \"MAR20\": 0,\n  \"MAR3\": 0,\n  \"MAR4\": 0,\n  \"MAR5\": 0,\n  \"MAR6\": 0,\n  \"MAR7\": 0,\n  \"MAR8\": 0,\n  \"MAR9\": 0,\n  \"MEX1\": 0,\n  \"MEX10\": 0,\n  \"MEX11\": 0,\n  \"MEX12\": 0,\n  \"MEX13\": 0,\n  \"MEX14\": 0,\n  \"MEX15\": 0,\n  \"MEX16\": 0,\n  \"MEX17\": 0,\n  \"MEX18\": 0,\n  \"MEX19\": 0,\n  \"MEX2\": 0,\n  \"MEX20\": 0,\n  \"MEX3\": 0,\n  \"MEX4\": 0,\n  \"MEX5\": 0,\n  \"MEX6\": 0,\n  \"MEX7\": 0,\n  \"MEX8\": 0,\n  \"MEX9\": 0,\n  \"NED1\": 0,\n  \"NED10\": 0,\n  \"NED11\": 0,\n  \"NED12\": 0,\n  \"NED13\": 0,\n  \"NED14\": 0,\n  \"NED15\": 0,\n  \"NED16\": 0,\n  \"NED17\": 0,\n  \"NED18\": 0,\n  \"NED19\": 0,\n  \"NED2\": 0,\n  \"NED20\": 0,\n  \"NED3\": 0,\n  \"NED4\": 0,\n  \"NED5\": 0,\n  \"NED6\": 0,\n  \"NED7\": 0,\n  \"NED8\": 0,\n  \"NED9\": 0,\n  \"POL1\": 0,\n  \"POL10\": 0,\n  \"POL11\": 0,\n  \"POL12\": 0,\n  \"POL13\": 0,\n  \"POL14\": 0,\n  \"POL15\": 0,\n  \"POL16\": 0,\n  \"POL17\": 0,\n  \"POL18\": 0,\n  \"POL19\": 0,\n  \"POL2\": 0,\n  \"POL20\": 0,\n  \"POL3\": 0,\n  \"POL4\": 0,\n  \"POL5\": 0,\n  \"POL6\": 0,\n  \"POL7\": 0,\n  \"POL8\": 0,\n  \"POL9\": 0,\n  \"POR1\": 0,\n  \"POR10\": 0,\n  \"POR11\": 0,\n  \"POR12\": 0,\n  \"POR13\": 0,\n  \"POR14\": 0,\n  \"POR15\": 0,\n  \"POR16\": 0,\n  \"POR17\": 0,\n  \"POR18\": 0,\n  \"POR19\": 0,\n  \"POR2\": 0,\n  \"POR20\": 0,\n  \"POR3\": 0,\n  \"POR4\": 0,\n  \"POR5\": 0,\n  \"POR6\": 0,\n  \"POR7\": 0,\n  \"POR8\": 0,\n  \"POR9\": 0,\n  \"QAT1\": 0,\n  \"QAT10\": 0,\n  \"QAT11\": 0,\n  \"QAT12\": 0,\n  \"QAT13\": 0,\n  \"QAT14\": 0,\n  \"QAT15\": 0,\n  \"QAT16\": 0,\n  \"QAT17\": 0,\n  \"QAT18\": 0,\n  \"QAT19\": 0,\n  \"QAT2\": 0,\n  \"QAT20\": 0,\n  \"QAT3\": 0,\n  \"QAT4\": 0,\n  \"QAT5\": 0,\n  \"QAT6\": 0,\n  \"QAT7\": 0,\n  \"QAT8\": 0,\n  \"QAT9\": 0,\n  \"SEN1\": 0,\n  \"SEN10\": 0,\n  \"SEN11\": 0,\n  \"SEN12\": 0,\n  \"SEN13\": 0,\n  \"SEN14\": 0,\n  \"SEN15\": 0,\n  \"SEN16\": 0,\n  \"SEN17\": 0,\n  \"SEN18\": 0,\n  \"SEN19\": 0,\n  \"SEN2\": 0,\n  \"SEN20\": 0,\n  \"SEN3\": 0,\n  \"SEN4\": 0,\n  \"SEN5\": 0,\n  \"SEN6\": 0,\n  \"SEN7\": 0,\n  \"SEN8\": 0,\n  \"SEN9\": 0,\n  \"SRB1\": 0,\n  \"SRB10\": 0,\n  \"SRB11\": 0,\n  \"SRB12\": 0,\n  \"SRB13\": 0,\n  \"SRB14\": 0,\n  \"SRB15\": 0,\n  \"SRB16\": 0,\n  \"SRB17\": 0,\n  \"SRB18\": 0,\n  \"SRB19\": 0,\n  \"SRB2\": 0,\n  \"SRB20\": 0,\n  \"SRB3\": 0,\n  \"SRB4\": 0,\n  \"SRB5\": 0,\n  \"SRB6\": 0,\n  \"SRB7\": 0,\n  \"SRB8\": 0,\n  \"SRB9\": 0,\n  \"SUI1\": 0,\n  \"SUI10\": 0,\n  \"SUI11\": 0,\n  \"SUI12\": 0,\n  \"SUI13\": 0,\n  \"SUI14\": 0,\n  \"SUI15\": 0,\n  \"SUI16\": 0,\n  \"SUI17\": 0,\n  \"SUI18\": 0,\n  \"SUI19\": 0,\n  \"SUI2\": 0,\n  \"SUI20\": 0,\n  \"SUI3\": 0,\n  \"SUI4\": 0,\n  \"SUI5\": 0,\n  \"SUI6\": 0,\n  \"SUI7\": 0,\n  \"SUI8\": 0,\n  \"SUI9\": 0,\n  \"TUN1\": 0,\n  \"TUN10\": 0,\n  \"TUN11\": 0,\n  \"TUN12\": 0,\n  \"TUN13\": 0,\n  \"TUN14\": 0,\n  \"TUN15\": 0,\n  \"TUN16\": 0,\n  \"TUN17\": 0,\n  \"TUN18\": 0,\n  \"TUN19\": 0,\n  \"TUN2\": 0,\n  \"TUN20\": 0,\n  \"TUN3\": 0,\n  \"TUN4\": 0,\n  \"TUN5\": 0,\n  \"TUN6\": 0,\n  \"TUN7\": 0,\n  \"TUN8\": 0,\n  \"TUN9\": 0,\n  \"URU1\": 0,\n  \"URU10\": 0,\n  \"URU11\": 0,\n  \"URU12\": 0,\n  \"URU13\": 0,\n  \"URU14\": 0,\n  \"URU15\": 0,\n  \"URU16\": 0,\n  \"URU17\": 0,\n  \"URU18\": 0,\n  \"URU19\": 0,\n  \"URU2\": 0,\n  \"URU20\": 0,\n  \"URU3\": 0,\n  \"URU4\": 0,\n  \"URU5\": 0,\n  \"URU6\": 0,\n  \"URU7\": 0,\n  \"URU8\": 0,\n  \"URU9\": 0,\n  \"USA1\": 0,\n  \"USA10\": 0,\n  \"USA11\": 0,\n  \"USA12\": 0,\n  \"USA13\": 0,\n  \"USA14\": 0,\n  \"USA15\": 0,\n  \"USA16\": 0,\n  \"USA17\": 0,\n  \"USA18\": 0,\n  \"USA19\": 0,\n  \"USA2\": 0,\n  \"USA20\": 0,\n  \"USA3\": 0,\n  \"USA4\": 0,\n  \"USA5\": 0,\n  \"USA6\": 0,\n  \"USA7\": 0,\n  \"USA8\": 0,\n  \"USA9\": 0,\n  \"WAL1\": 0,\n  \"WAL10\": 0,\n  \"WAL11\": 0,\n  \"WAL12\": 0,\n  \"WAL13\": 0,\n  \"WAL14\": 0,\n  \"WAL15\": 0,\n  \"WAL16\": 0,\n  \"WAL17\": 0,\n  \"WAL18\": 0,\n  \"WAL19\": 0,\n  \"WAL2\": 0,\n  \"WAL20\": 0,\n  \"WAL3\": 0,\n  \"WAL4\": 0,\n  \"WAL5\": 0,\n  \"WAL6\": 0,\n  \"WAL7\": 0,\n  \"WAL8\": 0,\n  \"WAL9\": 0\n}' in resp.data


def test_get_users_by_location(api):
    """Location returns all users associated with that location"""
    resp = api.get('/users/location/London')
    assert b'[\n  {\n    \"id\": \"89il2j3i9c\",\n    \"location\": \"London\",\n    \"username\": \"Sean\"\n  },\n  {\n    \"id\": \"lhw08vjbhh\",\n    \"location\": \"London\",\n    \"username\": \"Kornelia\"\n  },\n  {\n    \"id\": \"1ol48zwlo3\",\n    \"location\": \"London\",\n    \"username\": \"George\"\n  },\n  {\n    \"id\": \"vrntug0qoa\",\n    \"location\": \"London\",\n    \"username\": \"Brendan\"\n  }\n]' in resp.data


def test_post_individual_sticker(api):
    """Adds sticker code to user's string of sticker codes"""
    post_data = {"user": "89il2j3i9c"}

    resp = api.post(
                "/stickers/00",
                data=json.dumps(post_data),
                headers={"Content-Type": "application/json"})
    assert resp.status == "201 CREATED"
    assert b'\"00-1 FWC1-0 FWC2-0 FWC3-0 FWC4-0 FWC5-0 FWC6-0 FWC7-0 FWC8-0 FWC9-0 FWC10-0 FWC11-0 FWC12-0 FWC13-0 FWC14-0 FWC15-0 FWC16-0 FWC17-0 FWC18-0 FWC19-0 FWC20-0 FWC21-0 FWC22-0 FWC23-0 FWC24-0 FWC25-0 FWC26-0 FWC27-0 FWC28-0 FWC29-0 QAT1-0 QAT2-0 QAT3-0 QAT4-0 QAT5-0 QAT6-0 QAT7-0 QAT8-0 QAT9-0 QAT10-0 QAT11-0 QAT12-0 QAT13-0 QAT14-0 QAT15-0 QAT16-0 QAT17-0 QAT18-0 QAT19-0 QAT20-0 ECU1-1 ECU2-0 ECU3-0 ECU4-0 ECU5-0 ECU6-0 ECU7-0 ECU8-0 ECU9-0 ECU10-0 ECU11-0 ECU12-0 ECU13-0 ECU14-0 ECU15-0 ECU16-0 ECU17-0 ECU18-0 ECU19-0 ECU20-0 SEN1-0 SEN2-0 SEN3-0 SEN4-0 SEN5-0 SEN6-0 SEN7-0 SEN8-0 SEN9-0 SEN10-0 SEN11-0 SEN12-0 SEN13-0 SEN14-0 SEN15-0 SEN16-0 SEN17-0 SEN18-0 SEN19-0 SEN20-0 NED1-0 NED2-0 NED3-0 NED4-0 NED5-0 NED6-0 NED7-0 NED8-0 NED9-0 NED10-0 NED11-0 NED12-0 NED13-0 NED14-0 NED15-0 NED16-0 NED17-0 NED18-0 NED19-0 NED20-0 ENG1-0 ENG2-0 ENG3-0 ENG4-0 ENG5-0 ENG6-0 ENG7-0 ENG8-0 ENG9-0 ENG10-0 ENG11-0 ENG12-0 ENG13-0 ENG14-0 ENG15-0 ENG16-0 ENG17-0 ENG18-0 ENG19-0 ENG20-0 IRN1-0 IRN2-0 IRN3-0 IRN4-0 IRN5-0 IRN6-0 IRN7-0 IRN8-0 IRN9-0 IRN10-0 IRN11-0 IRN12-0 IRN13-0 IRN14-0 IRN15-0 IRN16-0 IRN17-0 IRN18-0 IRN19-0 IRN20-0 USA1-0 USA2-0 USA3-0 USA4-0 USA5-0 USA6-0 USA7-0 USA8-0 USA9-0 USA10-0 USA11-0 USA12-0 USA13-0 USA14-0 USA15-0 USA16-0 USA17-0 USA18-0 USA19-0 USA20-0 WAL1-0 WAL2-0 WAL3-0 WAL4-0 WAL5-0 WAL6-0 WAL7-0 WAL8-0 WAL9-0 WAL10-0 WAL11-0 WAL12-0 WAL13-0 WAL14-0 WAL15-0 WAL16-0 WAL17-0 WAL18-0 WAL19-0 WAL20-0 ARG1-0 ARG2-0 ARG3-0 ARG4-0 ARG5-0 ARG6-0 ARG7-0 ARG8-0 ARG9-0 ARG10-0 ARG11-0 ARG12-0 ARG13-0 ARG14-0 ARG15-0 ARG16-0 ARG17-0 ARG18-0 ARG19-0 ARG20-0 KSA1-0 KSA2-0 KSA3-0 KSA4-0 KSA5-0 KSA5-0 KSA7-0 KSA8-0 KSA9-0 KSA10-0 KSA11-0 KSA12-0 KSA13-0 KSA14-0 KSA15-0 KSA16-0 KSA17-0 KSA18-0 KSA19-0 KSA20-0 MEX1-0 MEX2-0 MEX3-0 MEX4-0 MEX5-0 MEX6-0 MEX7-0 MEX8-0 MEX9-0 MEX10-0 MEX11-0 MEX12-0 MEX13-0 MEX14-0 MEX15-0 MEX16-0 MEX17-0 MEX18-0 MEX19-0 MEX20-0 POL1-0 POL2-0 POL3-0 POL4-0 POL5-0 POL6-0 POL7-0 POL8-0 POL9-0 POL10-0 POL11-0 POL12-0 POL13-0 POL14-0 POL15-0 POL16-0 POL17-0 POL18-0 POL19-0 POL20-0 FRA1-0 FRA2-0 FRA3-0 FRA4-0 FRA5-0 FRA6-0 FRA7-0 FRA8-0 FRA9-0 FRA10-0 FRA11-0 FRA12-0 FRA13-0 FRA14-0 FRA15-0 FRA16-0 FRA17-0 FRA18-0 FRA19-0 FRA20-0 AUS1-0 AUS2-0 AUS3-0 AUS4-0 AUS5-0 AUS6-0 AUS7-0 AUS8-0 AUS9-0 AUS10-0 AUS11-0 AUS12-0 AUS13-0 AUS14-0 AUS15-0 AUS16-0 AUS17-0 AUS18-0 AUS19-0 AUS20-0 DEN1-0 DEN2-0 DEN3-0 DEN4-0 DEN5-0 DEN6-0 DEN7-0 DEN8-0 DEN9-0 DEN10-0 DEN11-0 DEN12-0 DEN13-0 DEN14-0 DEN15-0 DEN16-0 DEN17-0 DEN18-0 DEN19-0 DEN20-0 TUN1-0 TUN2-0 TUN3-0 TUN4-0 TUN5-0 TUN6-0 TUN7-0 TUN8-0 TUN9-0 TUN10-0 TUN11-0 TUN12-0 TUN13-0 TUN14-0 TUN15-0 TUN16-0 TUN17-0 TUN18-0 TUN19-0 TUN20-0 ESP1-0 ESP2-0 ESP3-0 ESP4-0 ESP5-0 ESP6-0 ESP7-0 ESP8-0 ESP9-0 ESP10-0 ESP11-0 ESP12-0 ESP13-0 ESP14-0 ESP15-0 ESP16-0 ESP17-0 ESP18-0 ESP19-0 ESP20-0 CRC1-0 CRC2-0 CRC3-0 CRC4-0 CRC5-0 CRC6-0 CRC7-0 CRC8-0 CRC9-0 CRC10-0 CRC11-0 CRC12-0 CRC13-0 CRC14-0 CRC15-0 CRC16-0 CRC17-0 CRC18-0 CRC19-0 CRC20-0 GER1-0 GER2-0 GER3-0 GER4-0 GER5-0 GER6-0 GER7-0 GER8-0 GER9-0 GER10-0 GER11-0 GER12-0 GER13-0 GER14-0 GER15-0 GER16-0 GER17-0 GER18-0 GER19-0 GER20-0 JPN1-0 JPN2-0 JPN3-0 JPN4-0 JPN5-0 JPN6-0 JPN7-0 JPN8-0 JPN9-0 JPN10-0 JPN11-0 JPN12-0 JPN13-0 JPN14-0 JPN15-0 JPN16-0 JPN17-0 JPN18-0 JPN19-0 JPN20-0 BEL1-0 BEL2-0 BEL3-0 BEL4-0 BEL5-0 BEL6-0 BEL7-0 BEL8-0 BEL9-0 BEL10-0 BEL11-0 BEL12-0 BEL13-0 BEL14-0 BEL15-0 BEL16-0 BEL17-0 BEL18-0 BEL19-0 BEL20-0 CAN1-0 CAN2-0 CAN3-0 CAN4-0 CAN5-0 CAN6-0 CAN7-0 CAN8-0 CAN9-0 CAN10-0 CAN11-0 CAN12-0 CAN13-0 CAN14-0 CAN15-0 CAN16-0 CAN17-0 CAN18-0 CAN19-0 CAN20-0 MAR1-0 MAR2-0 MAR3-0 MAR4-0 MAR5-0 MAR6-0 MAR7-0 MAR8-0 MAR9-0 MAR10-0 MAR11-0 MAR12-0 MAR13-0 MAR14-0 MAR15-0 MAR16-0 MAR17-0 MAR18-0 MAR19-0 MAR20-0 CRO1-0 CRO2-0 CRO3-0 CRO4-0 CRO5-0 CRO6-0 CRO7-0 CRO8-0 CRO9-0 CRO10-0 CRO11-0 CRO12-0 CRO13-0 CRO14-0 CRO15-0 CRO16-0 CRO17-0 CRO18-0 CRO19-0 CRO20-0 BRA1-0 BRA2-0 BRA3-0 BRA4-0 BRA5-0 BRA6-0 BRA7-0 BRA8-0 BRA9-0 BRA10-0 BRA11-0 BRA12-0 BRA13-0 BRA14-0 BRA15-0 BRA16-0 BRA17-0 BRA18-0 BRA19-0 BRA20-0 SRB1-0 SRB2-0 SRB3-0 SRB4-0 SRB5-0 SRB6-0 SRB7-0 SRB8-0 SRB9-0 SRB10-0 SRB11-0 SRB12-0 SRB13-0 SRB14-0 SRB15-0 SRB16-0 SRB17-0 SRB18-0 SRB19-0 SRB20-0 SUI1-0 SUI2-0 SUI3-0 SUI4-0 SUI5-0 SUI6-0 SUI7-0 SUI8-0 SUI9-0 SUI10-0 SUI11-0 SUI12-0 SUI13-0 SUI14-0 SUI15-0 SUI16-0 SUI17-0 SUI18-0 SUI19-0 SUI20-0 CMR1-0 CMR2-0 CMR3-0 CMR4-0 CMR5-0 CMR6-0 CMR7-0 CMR8-0 CMR9-0 CMR10-0 CMR11-0 CMR12-0 CMR13-0 CMR14-0 CMR15-0 CMR16-0 CMR17-0 CMR18-0 CMR19-0 CMR20-0 POR1-0 POR2-0 POR3-0 POR4-0 POR5-0 POR6-0 POR7-0 POR8-0 POR9-0 POR10-0 POR11-0 POR12-0 POR13-0 POR14-0 POR15-0 POR16-0 POR17-0 POR18-0 POR19-0 POR20-0 GHA1-0 GHA2-0 GHA3-0 GHA4-0 GHA5-0 GHA6-0 GHA7-0 GHA8-0 GHA9-0 GHA10-0 GHA11-0 GHA12-0 GHA13-0 GHA14-0 GHA15-0 GHA16-0 GHA17-0 GHA18-0 GHA19-0 GHA20-0 URU1-0 URU2-0 URU3-0 URU4-0 URU5-0 URU6-0 URU7-0 URU8-0 URU9-0 URU10-0 URU11-0 URU12-0 URU13-0 URU14-0 URU15-0 URU16-0 URU17-0 URU18-0 URU19-0 URU20-0 KOR1-0 KOR2-0 KOR3-0 KOR4-0 KOR5-0 KOR6-0 KOR7-0 KOR8-0 KOR9-0 KOR10-0 KOR11-0 KOR12-0 KOR13-0 KOR14-0 KOR15-0 KOR16-0 KOR17-0 KOR18-0 KOR19-0 KOR20-0\"' in resp.data
    
    
def test_remove_individual_sticker(api):
    post_data = {"user": "89il2j3i9c"}
    resp = api.put(
                "/stickers/00",
                data=json.dumps(post_data),
                headers={"Content-Type": "application/json"})
    assert resp.status == "301 MOVED PERMANENTLY"
    assert b'\"00-1 FWC1-0 FWC2-0 FWC3-0 FWC4-0 FWC5-0 FWC6-0 FWC7-0 FWC8-0 FWC9-0 FWC10-0 FWC11-0 FWC12-0 FWC13-0 FWC14-0 FWC15-0 FWC16-0 FWC17-0 FWC18-0 FWC19-0 FWC20-0 FWC21-0 FWC22-0 FWC23-0 FWC24-0 FWC25-0 FWC26-0 FWC27-0 FWC28-0 FWC29-0 QAT1-0 QAT2-0 QAT3-0 QAT4-0 QAT5-0 QAT6-0 QAT7-0 QAT8-0 QAT9-0 QAT10-0 QAT11-0 QAT12-0 QAT13-0 QAT14-0 QAT15-0 QAT16-0 QAT17-0 QAT18-0 QAT19-0 QAT20-0 ECU1-1 ECU2-0 ECU3-0 ECU4-0 ECU5-0 ECU6-0 ECU7-0 ECU8-0 ECU9-0 ECU10-0 ECU11-0 ECU12-0 ECU13-0 ECU14-0 ECU15-0 ECU16-0 ECU17-0 ECU18-0 ECU19-0 ECU20-0 SEN1-0 SEN2-0 SEN3-0 SEN4-0 SEN5-0 SEN6-0 SEN7-0 SEN8-0 SEN9-0 SEN10-0 SEN11-0 SEN12-0 SEN13-0 SEN14-0 SEN15-0 SEN16-0 SEN17-0 SEN18-0 SEN19-0 SEN20-0 NED1-0 NED2-0 NED3-0 NED4-0 NED5-0 NED6-0 NED7-0 NED8-0 NED9-0 NED10-0 NED11-0 NED12-0 NED13-0 NED14-0 NED15-0 NED16-0 NED17-0 NED18-0 NED19-0 NED20-0 ENG1-0 ENG2-0 ENG3-0 ENG4-0 ENG5-0 ENG6-0 ENG7-0 ENG8-0 ENG9-0 ENG10-0 ENG11-0 ENG12-0 ENG13-0 ENG14-0 ENG15-0 ENG16-0 ENG17-0 ENG18-0 ENG19-0 ENG20-0 IRN1-0 IRN2-0 IRN3-0 IRN4-0 IRN5-0 IRN6-0 IRN7-0 IRN8-0 IRN9-0 IRN10-0 IRN11-0 IRN12-0 IRN13-0 IRN14-0 IRN15-0 IRN16-0 IRN17-0 IRN18-0 IRN19-0 IRN20-0 USA1-0 USA2-0 USA3-0 USA4-0 USA5-0 USA6-0 USA7-0 USA8-0 USA9-0 USA10-0 USA11-0 USA12-0 USA13-0 USA14-0 USA15-0 USA16-0 USA17-0 USA18-0 USA19-0 USA20-0 WAL1-0 WAL2-0 WAL3-0 WAL4-0 WAL5-0 WAL6-0 WAL7-0 WAL8-0 WAL9-0 WAL10-0 WAL11-0 WAL12-0 WAL13-0 WAL14-0 WAL15-0 WAL16-0 WAL17-0 WAL18-0 WAL19-0 WAL20-0 ARG1-0 ARG2-0 ARG3-0 ARG4-0 ARG5-0 ARG6-0 ARG7-0 ARG8-0 ARG9-0 ARG10-0 ARG11-0 ARG12-0 ARG13-0 ARG14-0 ARG15-0 ARG16-0 ARG17-0 ARG18-0 ARG19-0 ARG20-0 KSA1-0 KSA2-0 KSA3-0 KSA4-0 KSA5-0 KSA5-0 KSA7-0 KSA8-0 KSA9-0 KSA10-0 KSA11-0 KSA12-0 KSA13-0 KSA14-0 KSA15-0 KSA16-0 KSA17-0 KSA18-0 KSA19-0 KSA20-0 MEX1-0 MEX2-0 MEX3-0 MEX4-0 MEX5-0 MEX6-0 MEX7-0 MEX8-0 MEX9-0 MEX10-0 MEX11-0 MEX12-0 MEX13-0 MEX14-0 MEX15-0 MEX16-0 MEX17-0 MEX18-0 MEX19-0 MEX20-0 POL1-0 POL2-0 POL3-0 POL4-0 POL5-0 POL6-0 POL7-0 POL8-0 POL9-0 POL10-0 POL11-0 POL12-0 POL13-0 POL14-0 POL15-0 POL16-0 POL17-0 POL18-0 POL19-0 POL20-0 FRA1-0 FRA2-0 FRA3-0 FRA4-0 FRA5-0 FRA6-0 FRA7-0 FRA8-0 FRA9-0 FRA10-0 FRA11-0 FRA12-0 FRA13-0 FRA14-0 FRA15-0 FRA16-0 FRA17-0 FRA18-0 FRA19-0 FRA20-0 AUS1-0 AUS2-0 AUS3-0 AUS4-0 AUS5-0 AUS6-0 AUS7-0 AUS8-0 AUS9-0 AUS10-0 AUS11-0 AUS12-0 AUS13-0 AUS14-0 AUS15-0 AUS16-0 AUS17-0 AUS18-0 AUS19-0 AUS20-0 DEN1-0 DEN2-0 DEN3-0 DEN4-0 DEN5-0 DEN6-0 DEN7-0 DEN8-0 DEN9-0 DEN10-0 DEN11-0 DEN12-0 DEN13-0 DEN14-0 DEN15-0 DEN16-0 DEN17-0 DEN18-0 DEN19-0 DEN20-0 TUN1-0 TUN2-0 TUN3-0 TUN4-0 TUN5-0 TUN6-0 TUN7-0 TUN8-0 TUN9-0 TUN10-0 TUN11-0 TUN12-0 TUN13-0 TUN14-0 TUN15-0 TUN16-0 TUN17-0 TUN18-0 TUN19-0 TUN20-0 ESP1-0 ESP2-0 ESP3-0 ESP4-0 ESP5-0 ESP6-0 ESP7-0 ESP8-0 ESP9-0 ESP10-0 ESP11-0 ESP12-0 ESP13-0 ESP14-0 ESP15-0 ESP16-0 ESP17-0 ESP18-0 ESP19-0 ESP20-0 CRC1-0 CRC2-0 CRC3-0 CRC4-0 CRC5-0 CRC6-0 CRC7-0 CRC8-0 CRC9-0 CRC10-0 CRC11-0 CRC12-0 CRC13-0 CRC14-0 CRC15-0 CRC16-0 CRC17-0 CRC18-0 CRC19-0 CRC20-0 GER1-0 GER2-0 GER3-0 GER4-0 GER5-0 GER6-0 GER7-0 GER8-0 GER9-0 GER10-0 GER11-0 GER12-0 GER13-0 GER14-0 GER15-0 GER16-0 GER17-0 GER18-0 GER19-0 GER20-0 JPN1-0 JPN2-0 JPN3-0 JPN4-0 JPN5-0 JPN6-0 JPN7-0 JPN8-0 JPN9-0 JPN10-0 JPN11-0 JPN12-0 JPN13-0 JPN14-0 JPN15-0 JPN16-0 JPN17-0 JPN18-0 JPN19-0 JPN20-0 BEL1-0 BEL2-0 BEL3-0 BEL4-0 BEL5-0 BEL6-0 BEL7-0 BEL8-0 BEL9-0 BEL10-0 BEL11-0 BEL12-0 BEL13-0 BEL14-0 BEL15-0 BEL16-0 BEL17-0 BEL18-0 BEL19-0 BEL20-0 CAN1-0 CAN2-0 CAN3-0 CAN4-0 CAN5-0 CAN6-0 CAN7-0 CAN8-0 CAN9-0 CAN10-0 CAN11-0 CAN12-0 CAN13-0 CAN14-0 CAN15-0 CAN16-0 CAN17-0 CAN18-0 CAN19-0 CAN20-0 MAR1-0 MAR2-0 MAR3-0 MAR4-0 MAR5-0 MAR6-0 MAR7-0 MAR8-0 MAR9-0 MAR10-0 MAR11-0 MAR12-0 MAR13-0 MAR14-0 MAR15-0 MAR16-0 MAR17-0 MAR18-0 MAR19-0 MAR20-0 CRO1-0 CRO2-0 CRO3-0 CRO4-0 CRO5-0 CRO6-0 CRO7-0 CRO8-0 CRO9-0 CRO10-0 CRO11-0 CRO12-0 CRO13-0 CRO14-0 CRO15-0 CRO16-0 CRO17-0 CRO18-0 CRO19-0 CRO20-0 BRA1-0 BRA2-0 BRA3-0 BRA4-0 BRA5-0 BRA6-0 BRA7-0 BRA8-0 BRA9-0 BRA10-0 BRA11-0 BRA12-0 BRA13-0 BRA14-0 BRA15-0 BRA16-0 BRA17-0 BRA18-0 BRA19-0 BRA20-0 SRB1-0 SRB2-0 SRB3-0 SRB4-0 SRB5-0 SRB6-0 SRB7-0 SRB8-0 SRB9-0 SRB10-0 SRB11-0 SRB12-0 SRB13-0 SRB14-0 SRB15-0 SRB16-0 SRB17-0 SRB18-0 SRB19-0 SRB20-0 SUI1-0 SUI2-0 SUI3-0 SUI4-0 SUI5-0 SUI6-0 SUI7-0 SUI8-0 SUI9-0 SUI10-0 SUI11-0 SUI12-0 SUI13-0 SUI14-0 SUI15-0 SUI16-0 SUI17-0 SUI18-0 SUI19-0 SUI20-0 CMR1-0 CMR2-0 CMR3-0 CMR4-0 CMR5-0 CMR6-0 CMR7-0 CMR8-0 CMR9-0 CMR10-0 CMR11-0 CMR12-0 CMR13-0 CMR14-0 CMR15-0 CMR16-0 CMR17-0 CMR18-0 CMR19-0 CMR20-0 POR1-0 POR2-0 POR3-0 POR4-0 POR5-0 POR6-0 POR7-0 POR8-0 POR9-0 POR10-0 POR11-0 POR12-0 POR13-0 POR14-0 POR15-0 POR16-0 POR17-0 POR18-0 POR19-0 POR20-0 GHA1-0 GHA2-0 GHA3-0 GHA4-0 GHA5-0 GHA6-0 GHA7-0 GHA8-0 GHA9-0 GHA10-0 GHA11-0 GHA12-0 GHA13-0 GHA14-0 GHA15-0 GHA16-0 GHA17-0 GHA18-0 GHA19-0 GHA20-0 URU1-0 URU2-0 URU3-0 URU4-0 URU5-0 URU6-0 URU7-0 URU8-0 URU9-0 URU10-0 URU11-0 URU12-0 URU13-0 URU14-0 URU15-0 URU16-0 URU17-0 URU18-0 URU19-0 URU20-0 KOR1-0 KOR2-0 KOR3-0 KOR4-0 KOR5-0 KOR6-0 KOR7-0 KOR8-0 KOR9-0 KOR10-0 KOR11-0 KOR12-0 KOR13-0 KOR14-0 KOR15-0 KOR16-0 KOR17-0 KOR18-0 KOR19-0 KOR20-0\"' in resp.data
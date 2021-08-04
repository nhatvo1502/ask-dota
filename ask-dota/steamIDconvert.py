steamid64ident = 76561197960265728

def commid_to_steamid(commid):
  steamid = []
  steamid.append('STEAM_0:')
  steamidacct = int(commid) - steamid64ident
  
  if steamidacct % 2 == 0:
      steamid.append('0:')
  else:
      steamid.append('1:')
  
  steamid.append(str(steamidacct // 2))
  
  return ''.join(steamid)

def commid_to_usteamid(commid):
    usteamid = []
    usteamid.append('[U:1:')
    steamidacct = int(commid) - steamid64ident
    
    usteamid.append(str(steamidacct) + ']')
    
    return ''.join(usteamid)

def commid_to_steam32id(commid):
    steam32id = []
    steamidacct = int(commid) - steamid64ident

    steam32id.append(str(steamidacct))

    return ''.join(steam32id)


print(commid_to_steam32id(76561198090759742))
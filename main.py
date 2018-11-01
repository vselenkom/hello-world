a={}
def parse_cdp_neighbors (line):
     
     
     if 'cdp' in line:
          pass        
     elif line.startswith(' '):
          pass
     elif line.startswith('Capability'):
          pass
     elif line.startswith('Device'):
          pass
     elif line.startswith('\n'):
          pass
     
     
     elif 'R S I' in line:
          result={}
          line=line.split()
          localDev=line[0]
          localInt=line[1]+line[2]
          RemoteDev=line[7]
          RemoteInt=line[8]+line[9]
          result[localDev,localInt]=tuple((RemoteDev+','+RemoteInt).split(','))
          
          return result
if __name__ == "__main__":
	with open('sw1_sh_cdp_neighbors.txt') as f:
		for stroki in f:
			try:
				a.update(parse_cdp_neighbors(stroki))
			except:
				pass
		print(a)

import binascii, sys, os
from rpcutils import rpcconnection

#creates binary cache array
binary_cache_list = []

#base command for all multichain json-rpc commands
base_command = 'sudo /usr/local/bin/multichain-cli auditchain %s' 

#create binary cache and output to txt file
create_binary_cache = base_command % ('createbinarycache > binarycache.txt 2>&1')

os.system(create_binary_cache)

#opens text file and extracts binary cache identifier and adds it to binary cache list
path = '/home/ubuntu/middleware-auditchain-io/binarycache.txt'
with open(path) as fp:
        for j, line in enumerate(fp):
                if j == 1:
                        print (line)
                        binary_cache_list.append(line)

#print to test if binary cache identifier stored
#print (binary_cache_list[0])

#convert test.pdf to data hex
filename = 'test.pdf'

# opens in binary mode to avoid two byte line endings on windows
with open(filename, 'rb') as f:
    content = f.read()

# Parses file and efficiently converts it to hex all at once
converted_hex = binascii.hexlify(content)
hex_utf = converted_hex.decode("utf-8") 

print (type(converted_hex))
print (type(hex_utf))

sys.stdout = open('hexoutput.txt', 'w')
print (hex_utf)

binary_cache_identifier = binary_cache_list[0]

#append pdf hex to binary cache
append_pdfhex_binarycache = base_command % ('createbinarycache > binarycache.txt 2>&1')
os.system(create_binary_cache)

#append pdf hex to binary cache
cmd = "ls -%s -%s"%(var1,var2)
#appendbinarycache identifier data-hex
append_pdfhex_binarycache = base_command % ('appendbinarycache %s %s')%(binary_cache_identifier,hex_utf)
os.system(append_pdfhex_binarycache)

# publishes pdf data via binary cache offchain 
#download_file = date_from_filename

publish_offchain = base_command % ('publish Stasis %s '{"cache":"%s"}' offchain')%(download_file,binary_cache_identifier)
#publish stream1 key6 '{"cache":"AxjQMTL5xxN"}' offchain

'''
#liststreamitems in PDF stream for unique key identifier
liststreamkeyitems stream1 key6

#peerstream stats
getchunkqueueinfo

#view first kb in hex once chunk queue empty
gettxoutdata txid 0 1024
'''
import enum

class CMDType(enum.Enum):
	OK = 0
	ERR = 1
	NOP = 254
	LOG = 2
	STOP = 3
	CONTINUE = 4
	CONNECT = 5
	DISCONNECT = 6
	SD = 7
	GETINFO = 8
	GETINFOREPLY = 9
	AUTHERR = 10
	NTLMAUTH = 11
	NTLMAUTHREPLY = 12
	NTLMCHALL = 13
	NTLMCHALLREPLY = 14
	KERBEROS = 15
	KERBEROSREPLY = 16
	SESSIONKEY = 17
	SESSIONKEYREPLY = 18
	SEQUENCE = 19
	SEQUENCEREPLY = 20

	LISTAGENTS = 100
	AGENTINFO = 101

	SDSRV = 200
	WRAPSSL = 201

	# File operations
	DIRLS = 300
	DIRMK = 301
	DIRRM = 302
	DIRCOPY = 303
	DIRMOVE = 304
	FILEOPEN = 305
	FILEREAD = 306
	FILEDATA = 307
	FILEENTRY = 308
	FILECOPY = 309
	FILEMOVE = 310
	FILERM = 311
	FILESTAT = 312




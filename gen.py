import base64
import nacl.public


def base(x):
	schluessel_bytes = bytes(x)
	schluessel_b32 = base64.b32encode(schluessel_bytes)
	assert schluessel_b32[-4:] == b'===='
	schluessel_b32 = schluessel_b32[:-4]
	s = schluessel_b32.decode('utf-8')
	return s

def main():
	privBob = nacl.public.PrivateKey.generate()
	pubBob = privBob.public_key

	print("Öffentlich: %s" % base(pubBob))
	print("Privat: %s" % base(privBob))

if __name__ == '__main__':
	exit(main())

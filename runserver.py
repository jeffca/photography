# app as application for wsgi
from jeffcaphotography import app as application

if __name__ == '__main__':
	application.run(host="0.0.0.0")
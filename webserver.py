import BaseHTTPServer

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    ''' Handle HTTP requests by returning a fixed page '''
    # Page to send back
    Page = '''\
<html>
<body>
<table>
<tr>  <td>Header</td>         <td>Value</td>          </tr>
<tr>  <td>Date and time</td>  <td>{date_time}</td>    </tr>
<tr>  <td>Client host</td>    <td>{client_host}</td>  </tr>
<tr>  <td>Client port</td>    <td>{client_port}s</td> </tr>
<tr>  <td>Command</td>        <td>{command}</td>      </tr>
<tr>  <td>Path</td>           <td>{path}</td>         </tr>
</table>
</body>
</html>
'''
    def do_GET(self):
        page = self.create_page()
	self.send_page(page)
    def create_page(self):
	values = {
	    'date_time'   : self.date_time_string(),
	    'client_host' : self.client_address[0],
            'client_port' : self.client_address[1],
            'command'     : self.command,
            'path'        : self.path
	}
	page = self.Page.format(**values)
	return page	
    def send_page(self,page):
        self.send_response(200)
        self.send_header("Content-Type","text/html")
        self.send_header("Content-Length",str(len(self.Page)))
        self.end_headers()

#-----------------------------------------------------------------

if __name__ == "__main__":
    serverAddress = ('127.0.0.1',8080)
    server = BaseHTTPServer.HTTPServer(serverAddress,RequestHandler)
    server.serve_forever()

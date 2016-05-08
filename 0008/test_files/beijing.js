//myColor is create by Yanghan,Jmrb.com
// writeCookie
function writeCookie(name, value, expires)
{
  var expire = "";
  if(expires != null)
  {
    expire = new Date((new Date()).getTime() + expires * 3600000);
    expire = "; expires=" + expire.toGMTString();
  }
  document.cookie = name + "=" + escape(value) + expire;
}

//readCookie
function readCookie(name)
{
  var cookieValue = "";
  var search = name + "=";
  if(document.cookie.length > 0)
  { 
    offset = document.cookie.indexOf(search);
    if (offset != -1)
    { 
      offset += search.length;
      end = document.cookie.indexOf(";", offset);
      if (end == -1) end = document.cookie.length;
      cookieValue = unescape(document.cookie.substring(offset, end))
    }
  }
  return cookieValue;
}

//setColor
function setColor(color_val) {
	document.getElementById('myTable').style.backgroundColor = color_val;
    writeCookie("bgColor_cookie", color_val, 24)
}

//getColor
function getColor() {
  myTable.style.backgroundColor = "#FFFFFF";
	var bg_color = readCookie("bgColor_cookie");
	if (bg_color != null) {
    	myTable.style.backgroundColor = bg_color
		//alert(bg_color);
	}
}

//setFontSize
function setFont(size_val) {
	document.getElementById('myFont').style.fontSize = size_val+"px";
	writeCookie("fontSize_cookis", size_val, 24)
}

//getFontSize
function getFontSize() {
	myFont.style.fontSize = "14px";
  var size = readCookie("fontSize_cookis");
	//alert(size);
	if (size != "") {
		myFont.style.fontSize = size+"px";
		}	
}

function PageInitialization()
{
  var s = "hello";
  document.write(s);
}

//	PageInitialization();

var currentpos,timer;
function initialize()
{
timer=setInterval("scrollwindow()",50);
}
function sc(){
clearInterval(timer);
}
function scrollwindow()
{
currentpos=document.body.scrollTop;
window.scroll(0,++currentpos);
if (currentpos != document.body.scrollTop)
sc();
}
//document.onmousedown=sc
//document.ondblclick=initialize
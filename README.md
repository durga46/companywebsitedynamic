# Dynamic Website Design for a Manufacturing Company
## AIM:
To design a dynamic website for a chip manufacturing company.

## DESIGN STEPS:
### Step 1: 
Requirement collection.
### Step 2:
Creating the layout using HTML and CSS.
### Step 3:
Updating the sample content.
### Step 4:
Choose the appropriate style and color scheme.
### Step 5:
Validate the layout in various browsers.
### Step 6:
Validate the HTML code.
### Step 7:
Create a database model and migrate the database.
### Step 8:
Retrieve data from database and display it in a dynamic webpage.
### Step 9:
Publish the website in the given URL

## PROGRAM:

### home.html
```
{% extends "website/base.html" %}

{% block content %}
    <div class="homecontent">    
    <h1>About Us</h1>
    <img src="/static/img/p1.png" alt="Building">
    <div class="contenttext">
    Zinc Pvt Ltd, provides a broad range of semiconductor and infrastructure software applications that serve the data center, networking, software, broadband, wireless, and storage and industrial markets. Common applications for its products include: data center networking, home connectivity, broadband access, telecommunications equipment, smartphones, base stations, data center servers and storage, factory automation, power generation and alternative energy systems, displays, and mainframe operations and management, and application software development. Some of Silicon's core technologies and products include:
    <ul>
        <li>Memory Chips</li>
        <li>SATA HDD</li>
        <li>SATA SSD </li>
        <li>Broadband Modems</li>
        <li>Wifi Devices</li>
        <li>Switching Devices</li>
        <li>Optical Sensors</li>
    </ul> 
    </div>
    </div>
{% endblock  %}

```
### people.html
```
% extends "website/base.html" %}

{% block content %}
<div>{
    <h1>Our team</h1>
    <div class="productitems">
        {% for people in peoples%}
        <div class="productitem">
            <div class="itemimage">
                <img src="{{ people.photo.url }}" alt="People photo">
            </div>
            <div class="itemname">{{ people.name }}</div>
            <div class="itemprice">{{ people.position }}</div>
        </div>
        {% endfor %}
    </div>
</div>
{% endblock  %}

```
### products.html
```
% extends "website/base.html" %}

{% block content %}
<div>{
    <h1>Our team</h1>
    <div class="productitems">
        {% for people in peoples%}
        <div class="productitem">
            <div class="itemimage">
                <img src="{{ people.photo.url }}" alt="People photo">
            </div>
            <div class="itemname">{{ people.name }}</div>
            <div class="itemprice">{{ people.position }}</div>
        </div>
        {% endfor %}
    </div>
</div>
{% endblock  %}

```
### contactus.html
```
{% extends "website/base.html" %}

{% block content %}<div>
    <h1>Contact details</h1>
    <div>
        <h2>Tamilnadu</h2>
            <h4>Mr.Abishek Bhalotia</h4>
            <h3>Phone Number:</h3>
            <h4>044-894532</h4>
            <h2>Kerala</h2>
            <h4>Mr.Anil agarval</h4>
            <h3>Phone Number:</h3>
            <h4>044-564980</h4>
            <h2>Karnataka</h2>
            <h4>Mr.Sharma</h4>
            <h3>Phone Number:</h3>
            <h4>8976543427</h4>
            <h2>Andra pradesh</h2>
            <h4>Mr.isak</h4>
            <h3>Phone Number:</h3>
            <h4>7865432913</h4>
            <h2>E-mail</h2>
            <h3>Zincpvtltd@gmail.com</h3>


       </div>
</div>

{% endblock  %}

```
## OUTPUT:
![output](./static/img/o1.png)

![output](./static/img/o2.png)

![output](./static/img/o3.png)

![output](./static/img/o4.png)

![output](./static/img/o5.png)

![output](./static/img/o6.png)

![output](./static/img/o7.png)

## CODE VALIDATION REPORT:
![output](./static/img/val1.png)

![output](./static/img/val2.png)

![output](./static/img/val3.png)

![output](./static/img/val4.png)

## RESULT:
Thus a website is designed for the chip manufacturing company and is hosted in the URL http://durgadevi.student.saveetha.in:8000/. HTML code is validated.
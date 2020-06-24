# eBook Project Documentation



#### Forms
'<form>' - defines a form

'<form>' inputs:
- '<label>'
- '<input>'

'<input>' types:
- text
- radio
- submit
- email
- number

input & label are used together to define the label of the form, and the type of data it received.

##### input type="text"

Here, label for the first box, which received 'text' type data, is "First name:". Then second box is "Last name:"
- 'for' & 'id' are used as reference markers

```
<form>
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname"><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname">
</form>
```


##### input type="radio"

Another input type is 'radio', which defines a multiple choice style selection.

```
<form>
  <input type="radio" id="male" name="gender" value="male">
  <label for="male">Male</label><br>
  <input type="radio" id="female" name="gender" value="female">
  <label for="female">Female</label><br>
  <input type="radio" id="other" name="gender" value="other">
  <label for="other">Other</label>
</form>
```
This code will generate a multiple choice form, where the labels are "Male", "Female", or "Other"

##### input type="submit"

This type defines a button to submit the form data to a form-handler.
- a form-handler is a usually page with a script for processing form data; like an "Order Confirmed!" page.

An 'action' attribute can be defined in the <form> element, stating the web url/path of the form-handler.
See below:

```
<form action="/action_page.php">
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname" value="John"><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname" value="Doe"><br><br>
  <input type="submit" value="Submit">
</form>
```
(if an action attribute is not defined, then the action is set to the current page)

function validate() {
   var name = document.getElementById("name").value;

   if (!name.match(/^[A-Za-z ]+$/)) {
      alert("Only letters or space allowed in name field");
      return false;
   }
   var email = document.getElementById("email").value;

   if (!email.match(/^\w+@\w+\.\w{3}$/)) {
      alert("Email must be in form aa@bbb.ccc");
      return false;

   }
   var subject = document.getElementById("subject").value;
   if (!subject.match(/^[A-Za-z ]+$/)) {
      alert("Only letters or spaces allowed in the subject field");
      return false;
   }

   var message = document.getElementById("message");
   if ( message.value=="" ) {
      message.value = "none";
   }

   return true;   
}

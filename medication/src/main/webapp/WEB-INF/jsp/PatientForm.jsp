<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
         pageEncoding="ISO-8859-1"%>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="fn" uri="http://java.sun.com/jsp/jstl/functions" %>

<html>
  <body>
    <%@include file="navbar.jsp"%>
    <div class="container mt-5">
      <div class="row">
        <div class="col-4 offset-2 mb-3">
          <h3 class="">Create new patient</h3>
        </div>
      </div>

      <div class="row">
        <div class="col-8 offset-2">
           <form:form method="POST" action="/patient" modelAttribute="patient">
                <div class="form-group row">
                    <form:label path="firstName" for="firstName" class="col-sm-2 col-form-label">Firstname</form:label>
                    <div class="col-sm-10">
                      <form:input path="firstName" type="text" class="form-control" id="firstName" placeholder="Firstname"/>
                    </div>
                </div>
                <div class="form-group row">
                    <form:label path="lastName" for="lastName" class="col-sm-2 col-form-label">Lastname</form:label>
                    <div class="col-sm-10">
                      <form:input path="lastName" type="text" class="form-control" id="lastName" placeholder="Lastname"/>
                    </div>
                </div>
                <div class="form-group row">
                    <form:label path="city" for="city" class="col-sm-2 col-form-label">City</form:label>
                    <div class="col-sm-10">
                      <form:input path="city" type="text" class="form-control" id="city" placeholder="City"/>
                    </div>
                </div>
                <div class="form-group row">
                    <form:label path="age" for="age" class="col-sm-2 col-form-label">Age</form:label>
                    <div class="col-sm-10">
                      <form:input path="age" type="text" class="form-control" id="age" placeholder="Age"/>
                    </div>
                </div>
                <div class="text-right">
                  <button type="submit" class="btn btn-primary">Save</button>
                </div>
           </form:form>
        </div>
      </div>
    </div>
  </body>
</html>
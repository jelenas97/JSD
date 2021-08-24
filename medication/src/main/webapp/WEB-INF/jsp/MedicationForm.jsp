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
          <h3 class="">Create new medication</h3>
        </div>
      </div>

      <div class="row">
        <div class="col-8 offset-2">
           <form:form method="POST" action="/medication" modelAttribute="medication">
                <div class="form-group row">
                    <form:label path="code" for="code" class="col-sm-2 col-form-label">Code</form:label>
                    <div class="col-sm-10">
                      <form:input path="code" type="text" class="form-control" id="code" placeholder="Code"/>
                    </div>
                </div>
                <div class="form-group row">
                    <form:label path="name" for="name" class="col-sm-2 col-form-label">Name</form:label>
                    <div class="col-sm-10">
                      <form:input path="name" type="text" class="form-control" id="name" placeholder="Name"/>
                    </div>
                </div>
                <div class="form-group row">
                    <form:label path="type" for="type" class="col-sm-2 col-form-label">Type</form:label>
                    <div class="col-sm-10">
                      <form:input path="type" type="text" class="form-control" id="type" placeholder="Type"/>
                    </div>
                </div>
                <div class="form-group row">
                    <form:label path="description" for="description" class="col-sm-2 col-form-label">Description</form:label>
                    <div class="col-sm-10">
                      <form:input path="description" type="text" class="form-control" id="description" placeholder="Description"/>
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
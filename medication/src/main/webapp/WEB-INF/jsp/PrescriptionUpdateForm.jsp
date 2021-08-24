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
          <h3 class="">Update prescription</h3>
        </div>
      </div>

      <div class="row">
        <div class="col-8 offset-2">
           <form:form method="POST" action="/prescription/update" modelAttribute="prescription">
                <div class="form-group row">
                    <form:label path="title" for="title" class="col-sm-2 col-form-label">Title</form:label>
                    <div class="col-sm-10">
                      <form:input path="title" type="text" class="form-control" id="title" placeholder="Title"/>
                    </div>
                </div>
                <div class="form-group row">
                    <form:label path="doctor" for="doctor" class="col-sm-2 col-form-label">Doctor</form:label>
                    <div class="col-sm-10">
                      <form:input path="doctor" type="text" class="form-control" id="doctor" placeholder="Doctor"/>
                    </div>
                </div>
                <div class="form-group row">
                <div class="col-sm-2">Valid</div>
                <div class="col-sm-10">
                  <div class="form-check">
                    <form:checkbox path="valid" class="form-check-input" id="gridCheck1"/>
                    <form:label path="valid" class="form-check-label" for="gridCheck1">
                      Valid
                    </form:label>
                  </div>
                </div>
                </div>
                <div class="text-right">
                  <button type="submit" class="btn btn-primary">Update</button>
                </div>
           </form:form>
        </div>
      </div>
    </div>
  </body>
</html>
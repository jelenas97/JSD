<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>

<html>
<body>
<%@include file="navbar.jsp" %>
    <div class="container mt-5">
      <div class="row">
        <div class="col-4 offset-2 mb-3">
          <h3 class="">List of all patient</h3>
        </div>
      </div>

      <div class="row">
        <div class="col-8 offset-2 mb-3">
            <table class="table table-sm">
                <thead>
                    <tr>
                    <th>Id</th>
                    <th>Firstname</th>
                    <th>Lastname</th>
                    <th>City</th>
                    <th>Age</th>
                    <th class="text-right">Update</th>
                    <th class="text-right">Delete</th>
                    </tr>
                </thead>
                <tbody>
                    <c:forEach items="${ PatientList }" var="patient">
                    <tr>
                    <td>${ patient.id }</td>
                    <td>${ patient.firstName }</td>
                    <td>${ patient.lastName }</td>
                    <td>${ patient.city }</td>
                    <td>${ patient.age }</td>

                          <td class="text-right">
                              <button class="btn btn-sm">

                                        <a href="/patient/update/${ patient.id }">Update</a>
                            </button>
                          </td>


                    <td class="text-right">
                      <button class="btn btn-sm">
  
                            <a href="/patient/delete/${ patient.id }">Delete</a>
                      </button>
                    </td>
                    </tr>
                    </c:forEach>
                </tbody>
            </table>
        </div>
      </div>
    </div>
</body>
</html>
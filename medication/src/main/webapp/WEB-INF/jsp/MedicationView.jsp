<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>

<html>
<body>
<%@include file="navbar.jsp" %>
    <div class="container mt-5">
      <div class="row">
        <div class="col-4 offset-2 mb-3">
          <h3 class="">Look at all medication</h3>
        </div>
      </div>

      <div class="row">
        <div class="col-8 offset-2 mb-3">
            <table class="table table-sm">
                <thead>
                    <tr>
                    <th>Id</th>
                    <th>Code</th>
                    <th>Name</th>
                    <th>Type</th>
                    <th>Description</th>
                    <th class="text-right">Delete</th>
                    </tr>
                </thead>
                <tbody>
                    <c:forEach items="${ MedicationList }" var="medication">
                    <tr>
                    <td>${ medication.id }</td>
                    <td>${ medication.code }</td>
                    <td>${ medication.name }</td>
                    <td>${ medication.type }</td>
                    <td>${ medication.description }</td>
                    <td class="text-right">
                        <button class="btn btn-sm">
                            <a href="/medication/delete/${ medication.id }">Delete</a>
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
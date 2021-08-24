<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>

<html>
<body>
<%@include file="navbar.jsp" %>
    <div class="container mt-5">
      <div class="row">
        <div class="col-4 offset-2 mb-3">
          <h3 class="">Look at all prescription</h3>
        </div>
      </div>

      <div class="row">
        <div class="col-8 offset-2 mb-3">
            <table class="table table-sm">
                <thead>
                    <tr>
                    <th>Id</th>
                    <th>Title</th>
                    <th>Doctor</th>
                    <th>Valid</th>
                    <th>Medications</th>
                    <th class="text-right">Delete</th>
                    </tr>
                </thead>
                <tbody>
                    <c:forEach items="${ PrescriptionList }" var="prescription">
                    <tr>
                    <td>${ prescription.id }</td>
                    <td>${ prescription.title }</td>
                    <td>${ prescription.doctor }</td>
                    <td>${ prescription.valid }</td>
                    <td>${ prescription.medications }</td>
                    <td class="text-right">
                        <button class="btn btn-sm">
                            <a href="/prescription/delete/${ prescription.id }">Delete</a>
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
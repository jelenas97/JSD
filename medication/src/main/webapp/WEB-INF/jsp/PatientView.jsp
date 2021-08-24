<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>

<html>
<body>
<%@include file="navbar.jsp" %>
    <div class="container mt-5">
      <div class="row">
        <div class="col-4 offset-2 mb-3">
          <h3 class="">Look at all patient</h3>
        </div>
      </div>

      <div class="row">
        <div class="col-8 offset-2 mb-3">
            <table class="table table-sm">
                <thead>
                    <tr>
                    <td>${ patient.id }</td>
                    <td>${ patient.firstName }</td>
                    <td>${ patient.lastName }</td>
                    <td>${ patient.city }</td>
                    <td>${ patient.age }</td>
                    <td class="text-right">
                        <button class="btn btn-sm">
                            <a href="/Patient/delete/${ patient.id }">Delete</a>
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
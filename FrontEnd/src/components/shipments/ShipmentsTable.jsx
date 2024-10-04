import { useEffect, useState } from "react";
import { fetchShipments } from "../../stores/api"; // Adjust the correct path
import shipmentsStore from "../../stores/useStore"; // Adjust the correct path

const ShipmentsList = () => {
  const { shipments, setShipments, filters } = shipmentsStore();

  const [page, setPage] = useState(1);
  const [next, setNext] = useState(null);
  const [previous, setPrevious] = useState(null);

  const [loading, setLoading] = useState(true); // حالة تحميل البيانات

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true); // تعيين حالة الجلب إلى true
        const data = await fetchShipments(filters, page);
        setShipments(data.results); // تعيين البيانات في الـ store
        setNext(data.next);
        setPrevious(data.previous);
      } catch (error) {
        console.error("Error fetching shipments:", error);
      } finally {
        setLoading(false); // بعد انتهاء الجلب بنجاح أو حدوث خطأ
      }
    };

    fetchData();
  }, [filters, setShipments, page]);

  const handleNextPage = () => {
    setPage(page + 1);
  };

  const handlePreviousPage = () => {
    setPage(page - 1);
  };

  const ShipmentsTable = ({ shipments }) => (
    <div className="container user-id-status-container mt-2">
      <table className="table table-striped table-bordered table-hover">
        <thead className="thead-dark">
          <tr>
            <th>رقم الشحنة</th>
            <th>اسم السائق</th>
            <th>اسم العميل</th>
            <th>المصدر</th>
            <th>الوجهه</th>
            <th>التحميل</th>
            <th>الوصول</th>
            <th>الاجرة</th>
            <th>المخرج</th>
            <th>حالة الشحنة</th>
          </tr>
        </thead>
        <tbody>
          {shipments.map((shipment) => (
            <tr key={shipment.id}>
              <td>{shipment.id}</td>
              <td>{shipment.driver.name}</td>
              <td>{shipment.customer_branch.customers.name}</td>
              {/* Accessing customer name */}
              <td>{shipment.customer_branch.city}</td>
              <td>{shipment.destination.name_ar}</td>
              <td>
                {new Date(shipment.created_at)
                  .toLocaleDateString("en-US", {
                    year: "numeric",
                    month: "2-digit",
                    day: "2-digit",
                  })
                  .replace(/(\d{2})\/(\d{2})\/(\d{4})/, "$3/$1/$2")}
              </td>
              <td>
                {new Date(shipment.actual_delivery_date)
                  .toLocaleDateString("en-US", {
                    year: "numeric",
                    month: "2-digit",
                    day: "2-digit",
                  })
                  .replace(/(\d{2})\/(\d{2})\/(\d{4})/, "$3/$1/$2")}
              </td>
              <td>{shipment.fare}</td>
              <td>{shipment.user.first_name}</td>
              <td>
                <button
                  className={`btn ${
                    shipment.status.name_en === "Shipped"
                      ? "btn-warning"
                      : shipment.status.name_en === "Delivered"
                      ? "btn-success"
                      : shipment.status.name_en === "Late"
                      ? "btn-danger"
                      : "btn-secondary"
                  }`}
                >
                  {shipment.status.name_ar}
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );

  return (
    <div>
      <div>
        {loading ? (
          <p>يتم جلب البيانات، يرجى الانتظار...</p> // عرض رسالة انتظار أثناء الجلب
        ) : (
          <ShipmentsTable shipments={shipments} /> // عرض الجدول بعد جلب البيانات
        )}
      </div>
      <div className="d-flex justify-content-center">
        <ul className="pagination">
          <li className={`page-item ${!previous ? "disabled" : ""}`}>
            <button
              className="page-link"
              onClick={handlePreviousPage}
              disabled={!previous}
            >
              Previous
            </button>
          </li>
          <li className="page-item">
            <span className="page-link">{page}</span>
          </li>
          <li className={`page-item ${!next ? "disabled" : ""}`}>
            <button
              className="page-link"
              onClick={handleNextPage}
              disabled={!next}
            >
              Next
            </button>
          </li>
        </ul>
      </div>
    </div>
  );
};

export default ShipmentsList;

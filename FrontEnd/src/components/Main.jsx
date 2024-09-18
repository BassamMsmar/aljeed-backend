import ShipmentsTable from "./shipments/ShipmentsTable";
import ShipmentsFilter from "./shipments/ShipmentsFilter";

const Main = () => {
  return (
    <main className="main">
      <div className="row">
        <div className="col-4 ">
          <ShipmentsFilter />
        </div>
        <div className="col-8">
          <ShipmentsTable />
        </div>
      </div>
    </main>
  );
};

export default Main;

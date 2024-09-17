import ShipmentsTable from "./shipments/ShipmentsTable";
import Filter from "./shipments/Filter";

const Main = () => {
  return (
    <main className="main">
      <div className="row">
        <div className="col-2 ">
          <Filter />
        </div>
        <div className="col-10">
          <ShipmentsTable />
        </div>
      </div>
    </main>
  );
};

export default Main;

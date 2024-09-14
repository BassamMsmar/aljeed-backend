import React from "react";
import ApexCharts from "apexcharts";
import * as echarts from "echarts";

const MainContent = () => {
  React.useEffect(() => {
    // ApexCharts initialization
    const reportsChart = new ApexCharts(
      document.querySelector("#reportsChart"),
      {
        series: [
          {
            name: "Sales",
            data: [31, 40, 28, 51, 42, 82, 56],
          },
          {
            name: "Revenue",
            data: [11, 32, 45, 32, 34, 52, 41],
          },
          {
            name: "Customers",
            data: [15, 11, 32, 18, 9, 24, 11],
          },
        ],
        chart: {
          height: 350,
          type: "area",
          toolbar: {
            show: false,
          },
        },
        markers: {
          size: 4,
        },
        colors: ["#4154f1", "#2eca6a", "#ff771d"],
        fill: {
          type: "gradient",
          gradient: {
            shadeIntensity: 1,
            opacityFrom: 0.3,
            opacityTo: 0.4,
            stops: [0, 90, 100],
          },
        },
        dataLabels: {
          enabled: false,
        },
        stroke: {
          curve: "smooth",
          width: 2,
        },
        xaxis: {
          type: "datetime",
          categories: [
            "2018-09-19T00:00:00.000Z",
            "2018-09-19T01:30:00.000Z",
            "2018-09-19T02:30:00.000Z",
            "2018-09-19T03:30:00.000Z",
            "2018-09-19T04:30:00.000Z",
            "2018-09-19T05:30:00.000Z",
            "2018-09-19T06:30:00.000Z",
          ],
        },
        tooltip: {
          x: {
            format: "dd/MM/yy HH:mm",
          },
        },
      }
    );

    reportsChart.render();

    // ECharts initialization
    const budgetChart = echarts.init(document.querySelector("#budgetChart"));
    budgetChart.setOption({
      legend: {
        data: ["Allocated Budget", "Actual Spending"],
      },
      radar: {
        indicator: [
          { name: "Sales", max: 6500 },
          { name: "Administration", max: 16000 },
          { name: "Information Technology", max: 30000 },
          { name: "Customer Support", max: 38000 },
          { name: "Development", max: 52000 },
          { name: "Marketing", max: 25000 },
        ],
      },
      series: [
        {
          name: "Budget vs spending",
          type: "radar",
          data: [
            {
              value: [4200, 3000, 20000, 35000, 50000, 18000],
              name: "Allocated Budget",
            },
            {
              value: [5000, 14000, 28000, 26000, 42000, 21000],
              name: "Actual Spending",
            },
          ],
        },
      ],
    });

    const trafficChart = echarts.init(document.querySelector("#trafficChart"));
    trafficChart.setOption({
      tooltip: {
        trigger: "item",
      },
      legend: {
        top: "5%",
        left: "center",
      },
      series: [
        {
          name: "Access From",
          type: "pie",
          radius: ["40%", "70%"],
          avoidLabelOverlap: false,
          label: {
            show: false,
            position: "center",
          },
          emphasis: {
            label: {
              show: true,
              fontSize: "18",
              fontWeight: "bold",
            },
          },
          labelLine: {
            show: false,
          },
          data: [
            { value: 1048, name: "Search Engine" },
            { value: 735, name: "Direct" },
            { value: 580, name: "Email" },
            { value: 484, name: "Union Ads" },
            { value: 300, name: "Video Ads" },
          ],
        },
      ],
    });

    return () => {
      // Cleanup chart instances
      reportsChart.destroy();
      budgetChart.dispose();
      trafficChart.dispose();
    };
  }, []);

  return (
    <main id="main" className="main">
      <div className="pagetitle">
        <h1>Dashboard</h1>
        <nav>
          <ol className="breadcrumb">
            <li className="breadcrumb-item">
              <a href="index.html">Home</a>
            </li>
            <li className="breadcrumb-item active">Dashboard</li>
          </ol>
        </nav>
      </div>

      <section className="section dashboard">
        <div className="row">
          <div className="col-lg-8">
            <div className="row">
              <div className="col-xxl-4 col-md-6">
                <div className="card info-card sales-card">
                  <div className="filter">
                    <a className="icon" href="#" data-bs-toggle="dropdown">
                      <i className="bi bi-three-dots"></i>
                    </a>
                    <ul className="dropdown-menu dropdown-menu-end dropdown-menu-arrow">
                      <li className="dropdown-header text-start">
                        <h6>Filter</h6>
                      </li>
                      <li>
                        <a className="dropdown-item" href="#">
                          Today
                        </a>
                      </li>
                      <li>
                        <a className="dropdown-item" href="#">
                          This Month
                        </a>
                      </li>
                      <li>
                        <a className="dropdown-item" href="#">
                          This Year
                        </a>
                      </li>
                    </ul>
                  </div>
                  <div className="card-body">
                    <h5 className="card-title">
                      Sales <span>| Today</span>
                    </h5>
                    <div className="d-flex align-items-center">
                      <div className="card-icon rounded-circle d-flex align-items-center justify-content-center">
                        <i className="bi bi-cart"></i>
                      </div>
                      <div className="ps-3">
                        <h6>145</h6>
                        <span className="text-success small pt-1 fw-bold">
                          12%
                        </span>
                        <span className="text-muted small pt-2 ps-1">
                          increase
                        </span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              {/* Revenue Card */}
              <div className="col-xxl-4 col-md-6">
                <div className="card info-card revenue-card">
                  {/* ... (similar structure as Sales Card) ... */}
                </div>
              </div>

              {/* Customers Card */}
              <div className="col-xxl-4 col-xl-12">
                <div className="card info-card customers-card">
                  {/* ... (similar structure as Sales Card) ... */}
                </div>
              </div>

              {/* Reports */}
              <div className="col-12">
                <div className="card">
                  <div className="card-body">
                    <h5 className="card-title">
                      Reports <span>/Today</span>
                    </h5>
                    <div id="reportsChart"></div>
                  </div>
                </div>
              </div>

              {/* Recent Sales */}
              <div className="col-12">
                <div className="card recent-sales overflow-auto">
                  {/* ... (Recent Sales card content) ... */}
                </div>
              </div>

              {/* Top Selling */}
              <div className="col-12">
                <div className="card top-selling overflow-auto">
                  {/* ... (Top Selling card content) ... */}
                </div>
              </div>
            </div>
          </div>

          {/* Right side columns */}
          <div className="col-lg-4">
            {/* Recent Activity */}
            <div className="card">
              {/* ... (Recent Activity card content) ... */}
            </div>

            {/* Budget Report */}
            <div className="card">
              <div className="card-body pb-0">
                <h5 className="card-title">
                  Budget Report <span>| This Month</span>
                </h5>
                <div
                  id="budgetChart"
                  style={{ minHeight: 400 }}
                  className="echart"
                ></div>
              </div>
            </div>

            {/* Website Traffic */}
            <div className="card">
              <div className="card-body pb-0">
                <h5 className="card-title">
                  Website Traffic <span>| Today</span>
                </h5>
                <div
                  id="trafficChart"
                  style={{ minHeight: 400 }}
                  className="echart"
                ></div>
              </div>
            </div>

            {/* News & Updates */}
            <div className="card">
              {/* ... (News & Updates card content) ... */}
            </div>
          </div>
        </div>
      </section>
    </main>
  );
};

export default MainContent;

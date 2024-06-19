import { createBrowserRouter } from "react-router-dom";
import MySliderComp from "../components/MySliderComp";
import MyImagesComp from "../components/MyImagesComp";
import ParentComp from "../components/ParentComp";
import ClickCounterComp from "../components/ClickCounterComp";
import PageNotFound from "../components/PageNotFound";
import listItems from "../components/listItems"
import UseRefHook from "../Hooks/UseRefHook";
import ReactHook from "../Hooks/ReactHook";
import UseStateHooks from "../Hooks/UseStateHooks";
import MainDashBoard from "../layout/MainDashBoard";
import UseEffectHook from "../Hooks/UseEffectHook";
import Dashboard from "../components/Dashboard";
import HoverCounterComp from "../components/HoverCounterComp"
import ToggleImgComp from "../Tasks/ToggleImgComp"
import ToggleMultiImgComp from "../Tasks/ToggleMultiImgComp"
import Chart from "../components/Chart";

const router = createBrowserRouter([
  {
    path: "maindashboard",
    element: <MainDashBoard />,
    children: [
      {
        path: "",
        element: <MySliderComp />,
      },
      {
        path: "myslider",
        element: <MySliderComp />,
      },
      {
        path: "myimages",
        element: <MyImagesComp />,
      },
      {
        path: "parent",
        element: <ParentComp />,
      },

      {
        path: "reacthook",
        element: <ReactHook />,
        children: [
          { path: "usestate", element: <UseStateHooks /> },
          { path: "useeffect", element: <UseEffectHook /> },
        ],
      },
    ],
  },
  {
    path: "material",
    element: <Dashboard />,children:[
        {
            path:"parent",element:<ParentComp/>
        },{
            path:"maindashboard",element:<>
            <Chart/>
            <MainDashBoard/></>,children:[

                {
                    path: "",
                    element: <MySliderComp />,
                  },
                  {
                    path: "myslider",
                    element: <MySliderComp />,
                  },
                  {
                    path: "myimages",
                    element: <MyImagesComp />,
                  },
                  {
                    path: "parent",
                    element: <ParentComp />,
                  },
            
                  {
                    path: "reacthook",
                    element: <ReactHook />,
                    children: [
                      { path: "usestate", element: <UseStateHooks /> },
                      { path: "useeffect", element: <UseEffectHook /> },
                    ],
                  },



            ]
        },{
            path:"parentchild",
            element:<ParentComp/>

        },{
            path:"clickcounter",
            element:<ClickCounterComp/>
        },
        {
            path:"hovercounter",
            element:<HoverCounterComp/>
        },
        {
            path: "myslider",
            element: <MySliderComp />,
          },
          {
            path: "myimages",
            element: <MyImagesComp />,
          },
          {
            path: "reacthook",
            element: <ReactHook />,
            children: [
              { path: "usestate", element: <UseStateHooks /> },
              { path: "useeffect", element: <UseEffectHook /> },
            ],
          },{
            path:"toggleimg",element:<ToggleImgComp/>
          }
          ,{
            path:"togglemulti",element:<ToggleMultiImgComp/>
          }


    ]
  },
  {
    path: "*",
    element: <PageNotFound />,
  },
]);

export default router;

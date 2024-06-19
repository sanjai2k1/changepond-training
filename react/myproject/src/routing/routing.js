import { createBrowserRouter } from "react-router-dom";
import MySliderComp from "../components/MySliderComp";
import MyImagesComp from "../components/MyImagesComp"
import ParentComp from "../components/ParentComp";
import ClickCounterComp from "../components/ClickCounterComp";
import PageNotFound from "../components/PageNotFound";

import UseRefHook from "../Hooks/UseRefHook";
import ReactHook from "../Hooks/ReactHook";
import UseStateHooks from "../Hooks/UseStateHooks";
import MainDashBoard from "../layout/MainDashBoard";
import UseEffectHook from "../Hooks/UseEffectHook";
import Dashboard from "../components/Dashboard";
const router = createBrowserRouter([
    {
        path: "maindashboard",
        element: <MainDashBoard />, children: [{
            path: "",
            element: <MySliderComp />
        },
        {
            path: "myslider",
            element: <MySliderComp />
        }, {
            path: "myimages", element: <MyImagesComp />
        },
        {
            path: "parent", element: <ParentComp />
        },

        {
            path: "reacthook", element: <ReactHook />, children: [
                { path: "usestate", element: <UseStateHooks /> },
                { path: "useeffect", element: <UseEffectHook /> }
            ]
        }]
    },{
path:"material",element:<Dashboard/>
    },
    {
        path: "*", element: <PageNotFound />
    }
])


export default router
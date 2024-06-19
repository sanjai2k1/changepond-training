import { createBrowserRouter } from "react-router-dom";
import MySliderComp from "../components/MySliderComp";
import MyImagesComp from "../components/MyImagesComp"

const router = createBrowserRouter([
    {
        path:"myslider",
        element:<MySliderComp/>
    },{
        path:"myimages",element:<MyImagesComp/>
    }
])


export default router
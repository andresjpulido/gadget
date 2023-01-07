# Gadget

Este proyecto consiste de componentes de software y hardware para capturar informacion desde unos sensores y visualizarla. Los sensores son implementados con arduino y los datos son enviados consumiendo servicios de nodejs. El cliente web esta desarrollado con [ReactJS](https://github.com/facebook/create-react-app).

El sistema consiste de tres maquinas:
- Componentes Arduino y Raspberry Pi
- API servicios en JS
- PC navegador web.

## Hardware

Los componentes de arduino con sensores.

### `Arduino`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `Raspberry pi`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

## Software

**Note: this is a one-way operation. Once you `gadget-js`, you can’t go back! `gadget-py` este es otro `gadget-ino` y el ultmo**

### `API`

El application programming interface (API) es instalado en el `servidor B`. It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.

Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `Web Client`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

El API contiene operaciones de autenticacion, If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

El gadget contiene una camara que transmite video, ademas los sensores de temperatura, distancia transmiten los datos al cliente web y al servidor que recopila informacion para reportes. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.
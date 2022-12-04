import { createApp } from 'vue'
import App from './App.vue'
import App2 from './App2.vue'
import router from './router'


const app = createApp(App)

app.use(router)

app.mount('#app')

// const app2 = createApp(App2)

// app2.use(router)

// app2.mount('#app2')



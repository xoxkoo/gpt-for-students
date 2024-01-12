/* eslint-disable vue/no-reserved-component-names */
/* eslint-disable vue/multi-word-component-names */
import { App } from 'vue';
import Button from 'primevue/button';
import Toast from 'primevue/toast';
import Panel from 'primevue/panel';
import FileUpload from 'primevue/fileupload';
import InputText from 'primevue/inputtext';
import Card from 'primevue/card';
import TabView from 'primevue/tabview';
import TabPanel from 'primevue/tabpanel';
import ScrollPanel from 'primevue/scrollpanel';

export default function registerComponents(app: App) {
	app.component('Button', Button);
	app.component('Toast', Toast);
	app.component('Panel', Panel);
	app.component('FileUpload', FileUpload);
	app.component('InputText', InputText);
	app.component('ScrollPanel', ScrollPanel);
	app.component('TabView', TabView);
	app.component('TabPanel', TabPanel);
	app.component('Card', Card);
}

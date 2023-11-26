import axios from 'axios';
import { ENDPOINT_URL } from '../utils/constants';
import { PDF_Request } from '../model';

const httpCLient = axios.create();

export const summarizationService = {
	url: `${ENDPOINT_URL}summarization`,

	async get(endopint: string) {
		return await httpCLient
			.get(`${this.url}${endopint}`)
			.then((response) => response.data)
			.catch((error) => console.log(error.response.data.message));
	},
	async post(endopint: string, data: any) {
		return await httpCLient
			.post(`${this.url}${endopint}`, data)
			.then((response) => response.data)
			.catch((error) => console.log(error.response.data.message));
	},
	async getWithQuery(query: string): Promise<PDF_Request | undefined> {
		return await this.post('/', { userInput: query });
	},
};

import axios from 'axios';
import { ENDPOINT_URL } from '../utils/constants';

const httpClient = axios.create();

export const chatService = {
	url: `${ENDPOINT_URL}chatter/`,
	// /chatter/?fileId=1&query="What is the document about?"

	async get(query: string) {
		return await httpClient
			.get(`${this.url}?${query}`)
			.then((response) => response.data)
			.catch((error) => console.log(error.response.data.message));
	},
	async post(endpoint: string, data: any) {
		return await httpClient
			.post(`${this.url}${endpoint}`, data)
			.then((response) => response.data)
			.catch((error) => console.log(error.response.data.message));
	},
	async queryFile(fileId: number, query: string): Promise<string> {
		return await this.get(`fileId=${fileId}&query=${query}`);
	},
};

<template>
	<div class="container mt-5 mx-auto">
		<div class="flex flex-col align-center">
			<TabView v-model:active-index="active">
				<TabPanel :header="$t(`summarizationTab.upload`)">
					<UploadBox @on-upload="onFileUpload" />
				</TabPanel>
				<TabPanel :header="$t(`summarizationTab.chat`)" :disabled="!fileId">
					<div class="message-list">
						<MessageBubble
							v-for="(bubble, index) in conversation"
							:key="index"
							:author="bubble.author"
							:message="bubble.message"
						/>
					</div>
					<div class="flex mt-10">
						<InputText
							v-model="message"
							@submit="onInputSubmit()"
							@keyup.enter="onInputSubmit()"
							ref="inputRef"
							type="text"
							class="w-full mr-5"
						/>
						<Button aria-label="refresh" icon="pi pi-refresh" @click="onReset"></Button>
					</div>
				</TabPanel>
				<TabPanel :header="$t(`summarizationTab.summarize`)" :disabled="!fileId"> </TabPanel>
			</TabView>
		</div>
	</div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { chatService } from '../services/chatService';
import { removeSpecialChar } from '../utils/inputUtils';
import UploadBox from '../components/UploadBox.vue';
import MessageBubble from '../components/MessageBubble.vue';
import { Conversation, ConversationAuthor } from '../model';
import { onMounted } from 'vue';
import { DEFAULT_MESSAGE } from '../utils/constants';
const message = ref<string>('');
const response = ref<string>('');
const conversation = ref<Conversation[]>([]);
const fileId = ref<number>(0);
const inputRef = ref<HTMLInputElement>(null);
const active = ref(0);

const onInputSubmit = async () => {
	if (!fileId.value) {
		fileId.value = JSON.parse(localStorage.getItem('fileId'));
	}
	if (removeSpecialChar(message.value)) {
		conversation.value.push({ author: ConversationAuthor.USER, message: message.value });
		const tmp = message.value;
		message.value = '';

		response.value = await chatService.queryFile(fileId.value, removeSpecialChar(tmp));
		conversation.value.push({ author: ConversationAuthor.GPT, message: response.value });
		saveConversation();
	}
};
const onFileUpload = (response: string) => {
	removeConversation();
	fileId.value = JSON.parse(response).id;

	localStorage.setItem('fileId', JSON.stringify(fileId.value));
	conversation.value.push(DEFAULT_MESSAGE[0]);
	saveConversation();
	active.value = 1;
};

const saveConversation = () => {
	localStorage.setItem('conversation', JSON.stringify(conversation.value));
};

const removeConversation = () => {
	if (localStorage.getItem('conversation')) localStorage.removeItem('conversation');
	if (localStorage.getItem('fileId')) localStorage.removeItem('fileId');

	conversation.value = [];
	fileId.value = undefined;
};

const fetchConversation = () => {
	if (localStorage.getItem('conversation')) conversation.value = JSON.parse(localStorage.getItem('conversation'));
};

const onReset = () => {
	removeConversation();
};

onMounted(() => {
	fetchConversation();

	if (!fileId.value && localStorage.getItem('fileId')) {
		fileId.value = JSON.parse(localStorage.getItem('fileId'));
	}
});
</script>

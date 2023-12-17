<template>
	<div class="container mt-20 mx-auto">
		<div class="flex flex-col align-center">
			<!-- <p class="text-sm">{{ $t('summarize.uploadYourFile') }}</p> -->
			<UploadBox v-if="!conversation.length && !fileId" @on-upload="onFileUpload" />

			<div v-else>
				<!-- <Panel class="mt-10" :header="$t('summarize.responseHeader')"> -->
				<!-- <template #header>
						<Button :label="$t('summarize.buttonReupload')" icon="pi pi-check" @click="summarizedResponse = ''" />
					</template> -->
				<div class="message-list">
					<MessageBubble
						v-for="(bubble, index) in conversation"
						:key="index"
						:author="bubble.author"
						:message="bubble.message"
					/>
				</div>
				<InputText
					v-model="message"
					@submit="onInputSubmit()"
					@keyup.enter="onInputSubmit()"
					ref="inputRef"
					type="text"
					class="mt-10 w-full"
				/>
				<!-- <template #footer>
						<Button :label="$t('summarize.submit')" icon="pi pi-check" @click="onInputSubmit()" />
					</template> -->
				<!-- </Panel> -->
			</div>
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
const message = ref<string>('');
const response = ref<string>('');
const conversation = ref<Conversation[]>([]);
const fileId = ref<number>(0);
const inputRef = ref<HTMLInputElement>(null);

const onInputSubmit = async () => {
	if (!fileId.value) {
		fileId.value = JSON.parse(localStorage.getItem('fileId'));
	}
	if (removeSpecialChar(message.value)) {
		console.log(conversation.value);

		conversation.value.push({ author: ConversationAuthor.USER, message: message.value });
		const tmp = message.value;
		message.value = '';

		response.value = await chatService.queryFile(fileId.value, removeSpecialChar(tmp));
		conversation.value.push({ author: ConversationAuthor.GPT, message: response.value });
		saveConversation();
	}
};
const onFileUpload = (response: string) => {
	fileId.value = JSON.parse(response).id;
	localStorage.setItem('fileId', JSON.stringify(fileId.value));
};

const saveConversation = () => {
	localStorage.setItem('conversation', JSON.stringify(conversation.value));
};

const fetchConversation = () => {
	if (localStorage.getItem('conversation')) conversation.value = JSON.parse(localStorage.getItem('conversation'));
};

onMounted(() => {
	fetchConversation();

	if (!fileId.value && localStorage.getItem('fileId')) {
		fileId.value = JSON.parse(localStorage.getItem('fileId'));
	}
});
</script>

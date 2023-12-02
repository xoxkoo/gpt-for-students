<template>
	<div class="card">
		<FileUpload
			name="summarize_file"
			:url="`${ENDPOINT_URL}upload/`"
			mode="advanced"
			:auto="true"
			@upload="onUpload"
			:multiple="false"
			accept=".pdf"
			:maxFileSize="1048576"
			:cancelLabel="$t('cancel')"
			:chooseLabel="$t('choose')"
			:uploadLabel="$t('upload')"
		>
			<template #empty>
				<p>{{ $t('dragAndDropFiles') }}</p>
			</template>
		</FileUpload>
	</div>
</template>

<script setup lang="ts">
import { ENDPOINT_URL } from '../utils/constants';

const onUpload = (request: any) => {
	// Handle the response here
	if (request.xhr.status == 200) {
		const response = JSON.parse(request.xhr.response);

		if (response && response.file_id) {
			const { file_id } = response;
			console.log(file_id);
		}
	}
};
</script>

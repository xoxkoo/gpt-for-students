<template>
	<div class="card">
		<!-- <Toast /> -->
		<FileUpload
			name="demo[]"
			url="/api/upload"
			@upload="console.log('a')"
			:multiple="true"
			accept="image/*"
			:maxFileSize="1000000"
		>
			<template #empty>
				<p>Drag and drop files to here to upload.</p>
			</template>
		</FileUpload>
	</div>
</template>

<script setup lang="ts">
// const onAdvancedUpload = () => {
// 	toast.add({ severity: 'info', summary: 'Success', detail: 'File Uploaded', life: 3000 });
// };
</script>

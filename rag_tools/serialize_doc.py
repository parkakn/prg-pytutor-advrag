
import re

class serialize_:

    # Serialize text chunks 
    def serialize_text_chunk(base_nodes):
        text_chunk_serialized = [] 
        for i in range(len(base_nodes)):
            # text chunks
            chunks = []
            for j in range(len(base_nodes[i])):
                dict_ = base_nodes[i][j].metadata
                dict_.update({ 
                        'start_char_idx':  base_nodes[i][j].start_char_idx,
                        'end_char_idx': base_nodes[i][j].end_char_idx})
                chunks.append(dict_)
            text_chunk_serialized.append(chunks)
        return text_chunk_serialized

    # Serialize object chunks 
    def serialize_object_chunk(obj_nodes):
        chunk_serialized_obj = [] 
        for i in range(len(obj_nodes)):
            chunks = []
            for j in range(len(obj_nodes[i])):
                # Add object node (Table summary and table)
                dict_ = {'section_summary': obj_nodes[i][j].obj.metadata['table_summary'],
                         'section title': obj_nodes[i][j].metadata['document_title'],
                         'start_char_idx':  obj_nodes[i][j].obj.start_char_idx,
                         'end_char_idx': obj_nodes[i][j].obj.end_char_idx}
                chunks.append(dict_)
            chunk_serialized_obj.append(chunks)
        return chunk_serialized_obj

    def combine_chunk(text_chunk, obj_chunk):
        chunk_full =[sublist1 + sublist2 for sublist1, sublist2 in zip(text_chunk, obj_chunk)]
        full_chunk = [] 
        for i in range(len(chunk_full)):
            # Sort Chunks in order and remove unnecessary parts 
            sorted_data = sorted(chunk_full[i], key=lambda x: (x['start_char_idx'], x['end_char_idx']))
            filtered_data = []
            for h in range(len(sorted_data)):
                if not any(sorted_data[h]['start_char_idx'] >= sorted_data[j]['start_char_idx'] and 
                        sorted_data[h]['end_char_idx'] <= sorted_data[j]['end_char_idx'] 
                        for j in range(len(sorted_data)) if h != j):
                    filtered_data.append(sorted_data[h])
            
            full_chunk.append(filtered_data)
        return full_chunk
            
    # Serialize full document 
    def serialize_doc(full_chunk,md,file_name):
        md_serialized = [] 
        for i in range(len(md)):

            # Extract document title from filename:
            match = re.search(r'Lecture Slides.*?/Week \d+', file_name[i])
            extracted_part = match.group() if match else ''

            dict_ = {'filename': file_name[i],  # Add document title 
                    'title': extracted_part,
                    'content': md[i][0].text,
                    'chunks': full_chunk[i]
                    }
            md_serialized.append(dict_)
        return md_serialized
    
    def content_for_embedding(cf,doc):
        embed_chunk_full = [] 
        for i in range(len(cf)):
            embed_chunk = [] 
            for j in range(len(cf[i])):
                result_string = "\n\n".join(f"{key}: {value}" for key, value in list(cf[i][j].items())[:-2])
                # Content from doc:
                content_list = "\n\ncontent: " + doc[i]['content'][cf[i][j]['start_char_idx']:cf[i][j]['end_char_idx']] 

                result_string  = result_string+content_list

                embed_chunk.append(result_string)
            embed_chunk_full.append(embed_chunk)
        return embed_chunk_full
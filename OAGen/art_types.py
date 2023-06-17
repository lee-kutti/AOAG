#!/usr/bin/python
#5static constexpr size_t kIRTPrevCount = kIsDebugBuild ? 7 : 3; if debug build 7 otherwise 3
kIsDebugBuild = 0
kIRTPrevCount = 3
art_types = {
    #art/runtime.h
    'Runtime' : [ 0x340, {
        'callee_save_methods_' : [0, ['uint64']],
        'pre_allocated_OutOfMemoryError_' : [ 32, ['GcRoot<mirror::Throwable>']],
        'pre_allocated_NoClassDefFoundError_' : [ 36, ['GcRoot<mirror::Throwable>']],
        'resolution_method_':[40,['pointer', ['ArtMethod']]],
        'imt_conflict_method_': [44,['pointer', ['ArtMethod']]],
        'imt_unimplemented_method_': [48, ['pointer', ['ArtMethod']]],
        'sentinel_' : [52, ['GcRoot<mirror::Object>']],
        'instruction_set_' : [56, ['Instruction Set']],
        'callee_save_method_frame_infos_': [60, ['QuickMethodFrameInfo']],
        'compiler_callbacks_': [108, ['pointer', ['CompilerCallbacks']]],
        'is_zygote_': [112, ['boolean']],
        'must_relocate_': [113, ['boolean']],
        'is_concurrent_gc_enabled_':[ 114, ['boolean']],
        'is_explicit_gc_disabled_':[ 115, ['boolean']],
        'dex2oat_enabled_':[116 , ['boolean']],
        'image_dex2oat_enabled_':[ 117, ['boolean']],
        'compiler_executable_':[120 , ['std::string']],
        'patchoat_executable_':[ 132 , ['std::string']],
        'compiler_options_':[ 144, ['std::vector<std::string>']],
        'image_compiler_options_':[ 156, ['std::vector<std::string>']],
        'image_location_':[ 168, ['std::string']],
        'boot_class_path_string_':[ 180, ['std::string']],
        'class_path_string_':[ 192, ['std::string']],
        'properties_':[ 204, ['std::vector<std::string>']],
        'agents_':[ 216, ['std::list<ti::Agent>']],
        'plugins_':[ 228, ['std::vector<Plugin>']],
        'default_stack_size_':[ 240, ['size_t']],
        'heap_':[244 , ['pointer', ['gc::Heap']]],
        'jit_arena_pool_':[ 248, ['std::unique_ptr<ArenaPool>']],
        'arena_pool_':[ 252, ['std::unique_ptr<ArenaPool>']],
        'low_4gb_arena_pool_':[ 256, ['std::unique_ptr<ArenaPool>']],
        'linear_alloc_':[ 260, ['std::unique_ptr<LinearAlloc>']],
        'max_spins_before_thin_lock_inflation_':[ 264, ['size_t']],
        'monitor_list_':[268 , ['pointer', ['MonitorList']]],
        'monitor_pool_':[ 272, ['pointer', ['MonitorPool']]],
        'thread_list_':[ 276, ['pointer', ['ThreadList']]],
        'intern_table_':[ 280,['pointer', ['InternTable']]],
        'class_linker_':[ 284, ['pointer', ['ClassLinker']]],
        'signal_catcher_':[ 288, ['pointer', ['SignalCatcher']]],
        'stack_trace_file_':[292 , ['std::string']],
        'java_vm_':[304 , ['pointer', ['JavaVMExt']]],
        'jit_':[ 308, ['pointer', ['Jit']]],
        'jit_options_':[ 312, ['pointer', ['JitOptions']]],
        'fault_message_lock_':[320 , ['Mutex']],
        'fault_message_':[ 360, [' std::string']],
        'threads_being_born_':[372 , ['size_t']],
        'shutdown_cond_':[376 , ['pointer', ['ConditionVariable']]],
        'shutting_down_':[ 380, ['boolean']],
        'shutting_down_started_':[ 381, ['boolean']],
        'started_':[ 382, ['boolean']],
        'finished_starting_':[ 383, ['boolean']],
        'vfprintf_':[ 384, ['jint']],
        'exit_':[ 388, ['pointer', ['void']]],
        'abort_':[ 392, ['pointer', ['void']]],
        'stats_enabled_':[ 396, ['boolean']],
        'stats_':[ 400, ['RuntimeStats']],
        'is_running_on_memory_tool_':[456 , ['const boolean']],
        'trace_config_':[ 460, ['pointer', ['TraceConfig']]],
        'instrumentation_':[ 464, ['Instrumentation']],
        'main_thread_group_':[680 , ['jobject']],
        'system_thread_group_':[684 , ['jobject']],
        'system_class_loader_':[ 688, ['jobject']],
        'dump_gc_performance_on_shutdown_':[692 , ['boolean']],
        'preinitialization_transaction_':[696 , ['pointer', ['Transaction']]],
        'verify_':[ 700, ['verifier::VerifyMode']],
        'allow_dex_file_fallback_':[ 701, ['boolean']],
        'cpu_abilist_':[ 704, [' std::vector<std::string>']],
        'target_sdk_version_':[ 716, ['int']],
        'implicit_null_checks_':[ 720, ['boolean']],
        'implicit_so_checks_':[721 , ['boolean']],
        'implicit_suspend_checks_':[ 722, ['boolean']],
        'no_sig_chain_':[ 723, ['boolean']],
        'force_native_bridge_':[ 724, ['boolean']],
        'is_native_bridge_loaded_':[ 725, ['boolean']],
        'is_native_debuggable_':[ 726, ['boolean']],
        'is_java_debuggable_':[ 727, ['boolean']],
        'zygote_max_failed_boots_':[ 728, ['uint']],
        'experimental_flags_':[ 732, ['ExperimentalFlags']],
        'fingerprint_':[ 736, ['std::string']],
        'oat_file_manager_':[748 , ['pointer', ['OatFileManager']]],
        'is_low_memory_mode_':[ 752, ['boolean']],
        'safe_mode_':[ 753, ['boolean']],
        'dump_native_stack_on_sig_quit_':[754 , ['boolean']],
        'pruned_dalvik_cache_':[ 755, ['boolean']],
        'process_state_':[ 756 , ['ProcessState']],
        'zygote_no_threads_':[ 760, ['boolean']],
        'env_snapshot_':[764, ['EnvSnapshot']],
        'system_weak_holders_':[780, ['std::vector<gc::AbstractSystemWeakHolder*>']],
        'cha_': [792, ['pointer', ['ClassHierarchyAnalysis']]],
        'callbacks_': [796, ['pointer', ['RuntimeCallbacks']]],
        'deoptimization_counts_': [800, ['std::atomic<uint32_t>']],
      }],
     'ThreadList' : [ 0x208c, {
        'allocated_ids_' : [0, ['std::bitset<kMaxThreadId>']],
        'list_' :[8192,['std::list<Thread*>']],
        'suspend_all_count_':[8204, ['int']],
        'debug_suspend_all_count_' : [8208, ['int']],
        'unregistering_count_':[8212, ['int']],
        'suspend_all_historam_': [8216, ['Histogram<uint64_t>']],
        'long_suspend_': [8316, ['boolean']],
        'thread_suspend_timeout_ns_' : [8320, ['const uint64_t']],
        'empty_checkpoint_barrier_': [8328, ['pointer', ['Barrier']]],
        }],
     'JavaVMExt': [0x88, {
      'DW_TAG_inheritance'  : [0, ['pointer']],
      'runtime_' : [4,['pointer', ['Runtime']]],
      'check_jni_abort_hook_' : [ 8,['void']],
      'check_jni_abort_hook_data_' : [12 ,['pointer', ['void']]],
      'check_jni_' : [ 16,['boolean']],
      'force_copy_' :[ 17,['boolean']],
      'tracing_enabled_' : [ 18,['const bool']],
      'trace_' : [ 20,['const std:string']],
      'globals_' : [ 32,['IndirectReferenceTable']],
      'libraries_' : [ 64,['pointer', ['Libraries']]],
      'unchecked_functions_' : [68 ,['pointer', ['const JNIInvokeInterface']]],
     'weak_globals_' : [ 72,['IndirectReferenceTable']],
     'allow_accessing_weak_globals_' : [104 ,['Atomic<bool>']],
      'weak_globals_add_condition_' : [ 108,['ConditionVariable']],
      'env_hooks_' : [124 ,['std::vector<GetEnvHook>']],
     }],
     'IndirectReferenceTable' : [ 0x20,{
         'segment_state_':[0, ['IRTSegmentState']],
         'table_mem_map_': [4, ['pointer', ['MemMap']]],
         'table_': [8, ['pointer', ['IrtEntry']]],
         'kind_':[12, ['const IndirectRefKind']],
         'max_entries_': [16, ['size_t']],
         'current_num_holes_':[20, ['size_t']],
         'last_known_previous_state_': [24, ['IRTSegmentState']],
         'resizable_': [28, ['ResizableCapacity']],
     }],
    'IrtEntry' :[ 0x10,{
    'serial_': [0, ['uint']],
    'references_':[4, ['GcRoot<mirror::Object>[kIRTPrevCount]']],
    }],
    'IRTSegmentState' : [0x4,{
        'top_index':[0,['uint']],
    }],
    'GcRoot<art::mirror::Object>' : [0x4,{
        'root_':[0,['CompressedReference<art::mirror::Object>']],
    }],
    'CompressedReference<art::mirror::Object>':[0x4, {
        'DW_TAG_inheritance': [0, ['']],
    }],
    'ObjectReference<false, art::mirror::Object>':[0x4, {
        'reference_': [0, ['uint']],
    }],
    'Object' : [0x8 , {
     'klass_':[0, ['HeapReference<Class>']],
     'monitor_':[4,['uint']],
    }],
    'Class_Obj' : [ 0x78, {
     'inheritance':[ 0,['Object']],
     'class_loader_':[8, ['HeapReference<ClassLoader>']],
     'component_type_':[12 ,['HeapReference<Class>']],
     'dex_cache_':[ 16,['HeapReference<DexCache>']],
     'ext_data_':[20 ,['HeapReference<ClassExt>']],
     'iftable_':[ 24,['HeapReference<IfTable>']],
        'name_':[28 ,['HeapReference<String>']],
        'super_class_':[32 ,['HeapReference<Class>']],
        'vtable_':[ 36,['HeapReference<PointerArray>']],
        'ifields_':[ 40,['uint64']],
        'methods_':[ 48,['uint64']],
        'sfields_':[56 ,['uint64']],
        'access_flags_':[64 ,['uint']],
        'class_flags_':[68 ,['uint']],
        'class_size_':[ 72,['uint']],
        'clinit_thread_id_':[76 ,['pid_t']],
        'dex_class_def_idx_':[ 80,['int']],
        'dex_type_idx_':[ 84,['int']],
        'num_reference_instance_fields_':[ 88,['uint']],
        'num_reference_static_fields_':[ 92,['uint']],
        'object_size_':[ 96,['uint']],
        'object_size_alloc_fast_path_':[100,['uint']],
        'primitive_type_':[104 ,['uint']],
        'reference_instance_offsets_':[108 ,['uint']],
        'status_':[ 112,['Status']],
        'copied_methods_offset_':[116 ,['uint16']],
        'virtual_methods_offset_':[ 118,['uint16']],
    }],
    'String_Obj':[0x10,{
     'inheritance':[0 ,['Object']],
     'count_':[8 ,['int']],
     'hash_code_':[ 16,['uint']],
    }],
    'Field':[0x20,{
        'inheritance':[0 ,['Object']],
        'padding_':[10 ,['uint8']],
        'declaring_class_':[12 ,['HeapReference<mirror::Class>']],
        'type_':[16 ,['HeapReference<mirror::Class>']],
        'access_flags_':[20 ,['int']],
        'dex_field_index_':[24 ,['int']],
        'offset_':[ 28,['int']],
    }],
    'ArtField':[0x10,{
        'declaring_class_':[0 ,['GcRoot<mirror::Class>']],
        'access_flags_':[4 ,['uint']],
        'field_dex_idx_':[8 ,['uint']],
        'offset_':[ 12,['uint']],
    }],
    'ArtMethod':[0x20,{
        'declaring_class_':[0,['GcRoot<mirror::Class>']],
        'access_flags_':[4,['std::atomic<std::uint32_t>']],
        'dex_code_item_offset_':[8,['uint']],
        'dex_method_index_':[12,['uint']],
        'method_index_':[16,['uint16']],
        'hotness_count_' :[18,['uint16']],
        'ptr_sized_fields_':[ 20,['PtrSizedFields']],
    }],
    'PtrSizedFields':[0xc,{
        'dex_cache_resolved_methods_': [0,['pointer', ['pointer', ['MonitorList']]]],
        'data_':[4,['pointer', ['void']]],
        'entry_point_from_quick_compiled_code_':[8, ['pointer', ['void']]],
    }],
    'struct_tls32_': [0x40,{
        'state_and_flags':[0,['union']],
        'suspend_count':[4,['int']],
        'debug_suspend_count':[8,['int']],
        'thin_lock_thread_id':[12,['uint']],
        'tid':[16,['uint']],
        'daemon':[20,['const bool32']],
        'throwing_OutOfMemoryError':[24,['bool32']],
        'no_thread_suspension':[28,['uint']],
        'thread_exit_check_count':[32,['uint']],
        'handling_signal_':[36,['bool32']],
        'is_transitioning_to_runnable':[ 40,['bool32']],
        'ready_for_debug_invoke':[ 44,['bool32']],
        'debug_method_entry_':[48 ,['bool32']],
        'is_gc_marking':[ 52,['bool32']],
        'weak_ref_access_enabled':[ 56,['bool32']],
        'disable_thread_flip_count':[ 64,['uint']],
    }],
    'struct_tls64_': [0x40,{
        'trace_clock_base':[ 0,['uint64']],
        'stats':[8 ,['RuntimeStats']], #Runtime Stats, size 0x38 bytes
    }],
    'struct_tlsPtr_': [0x480,{
        'card_table':[0,['pointer', ['uint8']]],
        'exception':[4,['pointer', ['mirror::Throwable']]],
        'stack_end':[8,['pointer', ['uint8']]],
        'managed_stack':[12,['ManagedStack']],
        'suspend_trigger':[24 ,['pointer', ['uintptr_t']]],
        'jni_env':[28 ,['pointer', ['JNIEnvExt']]],
        'tmp_jni_env':[ 32,['pointer', ['JNIEnvExt']]],
        'self':[36 ,['pointer', ['Thread']]],
        'opeer':[40 ,['pointer', ['mirror::Object']]],
        'jpeer':[44 ,['jobject']],
        'stack_begin':[ 48,['pointer', ['uint8']]],
        'stack_size':[ 52,['size_t']],
        'deps_or_stack_trace_sample':[56 ,['union']],
        'wait_next':[ 60,['pointer', ['Thread']]],
        'monitor_enter_object':[64 ,['pointer', ['mirror::Object']]],
        'top_handle_scope':[68 ,['pointer', ['BaseHandleScope']]],
        'class_loader_override':[72 ,['jobject']],
        'long_jump_context':[76 ,['pointer', ['Context']]],
        'instrumentation_stack':[80 ,['pointer', ['std::deque<instrumentation::InstrumentationStackFrame>']]],
        'debug_invoke_req':[84 ,['pointer', ['DebugInvokeReq']]],
        'single_step_control':[88 ,['pointer', ['SingleStepControl']]],
        'stacked_shadow_frame_record':[92 ,['pointer', ['StackShadowFrameRecord']]],
        'deoptimization_context_stack':[ 96,['pointer', ['DeoptimizationContextRecord']]],
        'frame_id_to_shadow_frame':[ 100,['pointer', ['FrameIdToShadowFrame']]],
        'name':[104 ,['pointer', ['std::string']]],
        'pthread_self':[108 ,['pthread_t']],
        'last_no_thread_suspension_cause':[112 ,['pointer', ['const char']]],
        'checkpoint_function':[116 ,['pointer', ['Closure']]],
        'active_suspend_barriers':[120 ,['pointer', ['AtomicInteger']]],
        'thread_local_start':[ 132,['pointer', ['uint8']]],
        'thread_local_pos':[136 ,['pointer', ['uint8']]],
        'thread_local_end':[140 ,['pointer', ['uint8']]],
        'thread_local_limit':[ 144,['pointer', ['uint8']]],
        'thread_local_objects':[148 ,['size_t']],
        'jni_entrypoints':[ 152,['JniEntryPoints']],
        'quick_entrypoints':[156 ,['QuickEntryPoints']],
        'mterp_current_ibase':[ 800,['pointer', ['void']]],
        'mterp_default_ibase':[804 ,['pointer', ['void']]],
        'mterp_alt_ibase':[808 ,['pointer', ['void']]],
        'rosalloc_runs':[ 812,['pointer', ['void']]],
        'thread_local_alloc_stack_top':[876 ,['pointer', ['StackReference<mirror::Object>']]],
        'thread_local_alloc_stack_end':[880 ,['pointer', ['StackReference<mirror::Object>']]],
        'held_mutexes':[884 ,['pointer', ['BaseMutex']]],
        'flip_function':[ 1140,['pointer', ['Closure']]],
        'method_verifier':[ 1144,['pointer', ['verifier::MethodVerifier']]],
        'thread_local_mark_stack':[1148 ,['pointer', ['gc::accounting::AtomicStack<mirror::Object>']]],
    }],
    'Thread' : [0x528,{
        'tls32_':[0,['struct_tls32_']],  #starting from location 0, size 0x40 bytes
        'tls64_':[64,['struct_tls64_']], #starting from location 64, size 0x40 bytes
        'tlsPtr_':[128,['struct_tlsPtr_']],#starting from location 128, size 0x480 bytes
        'wait_mutex_':[1280,['pointer', ['Mutex']]],
        'wait_cond_':[1284,['pointer', ['ConditionVariable']]],
        'wait_monitor_':[1288,['pointer', ['Monitor']]],
        'interrupted_':[1292,['boolean']],
        'debug_disallow_read_barrier_':[1293,['uint8']],
        'poison_object_cookie_': [1296,['uintptr_t']],
        'checkpoint_overflow_': [1300,['std::list<Closure*>']],
        'custom_tls_': [1312,['pointer', ['void']]],
        'can_call_into_java_':[ 1316,['boolean']],
    }],
    'DexCache':[0x88,{
        'inheritance':[0,['Object']],
        'location_':[8,['HeapReference<String>']],
        'num_resolved_call_sites_':[12,['uint']],
        'dex_file_':[16,['uint64']],
        'resolved_call_sites_':[24,['uint64']],
        'resolved_fields_':[32,['uint64']],
        'resolved_method_types_':[40,['uint64']],
        'resolved_methods_':[48,['uint64']],
        'resolved_types_':[56,['uint64']],
        'strings_':[64,['uint64']],
        'num_resolved_fields_':[72,['uint']],
        'num_resolved_method_types_':[76,['uint']],
        'num_resolved_methods_':[80,['uint']],
        'num_resolved_types_':[84 ,['uint']],
        'num_strings_':[88,['uint']],
    }],
    'FieldId':[0x8, {
        'class_idx_':[0,['dex::TypeIndex']],
        'type_idx_':[2,['dex::TypeIndex']],
        'name_idx_':[4,['dex::StringIndex']],
    }],
    'StringId':[0x4, {
        'string_data_off_': [0,['uint']],
    }],
    'TypeId':[0x4, {
        'descriptor_idx_': [0,['dex::StringIndex']],
    }],
    'MethodId':[0x8, {
        'class_idx_':[0,['dex::TypeIndex']],
        'proto_idx_':[2,['uint16']],
        'name_idx_':[4,['dex::StringIndex']],
    }],
    'ProtoId':[0xc, {
        'shorty_idx_':[0,['dex::StringIndex']],
        'return_type_idx_':[4,['dex::TypeIndex']],
        'pad_':[6,['uint16']],
        'parameter_off_':[8,['uint']],
    }],
    'ClassDef':[0x20, {
        'class_idx_':[0,['dex::TypeIndex']],
        'pad1_':[2,['uint16']],
        'access_flags':[4,['uint']],
        'superclass_idx':[8,['dex::TypeIndex']],
        'pad2_':[10,['uint16']],
        'interfaces_off_':[12,['uint']],
        'source_file_idx_':[16,['dex::StringIndex']],
        'annotations_off_':[20,['uint']],
        'class_data_off_':[24,['uint']],
        'static_values_off_':[28,['uint']],
    }],
    'DexFile':[0x50,{
        'begin_':[4,['pointer', ['uint8']]],
        'size_': [8,['size_t']],
        'location_':[12,['std::string']],
        'location_checksum_': [24,['int']],
        'mem_map_':[28,['pointer', ['MemMap']]],
        'header_':[32,['pointer', ['Header']]],
        'string_ids_':[36,['pointer', ['StringId']]],
        'type_ids_':[40,['pointer', ['TypeId']]],
        'field_ids_':[44,['pointer', ['FieldId']]],
        'method_ids_':[48,['pointer', ['MethodId']]],
        'proto_ids_':[52,['pointer', ['ProtoId']]],
        'class_defs_':[56,['pointer', ['ClassDef']]],
        'method_handles_':[ 60,['pointer', ['MethodHandleItem']]],
        'num_method_handles_':[64,['size_t']],
        'call_site_ids_':[68,['pointer', ['CallSiteIdItem']]],
        'num_call_site_ids_':[72,['size_t']],
        'oat_dex_file_':[76,['pointer', ['OatDexFile']]],
    }],
    'AllocSpace': [ 0x24 ,{
        '_vptr$AllocSpace':[36, ['pointer', ['virtual']]],
    }],
    'ContinuousSpace': [0x20, {
        'Space':[0,['Space']],
        'begin_':[20,['pointer', ['uint8']]],
        'end_':[24,['Atomic<uint8_t*>']],
        'limit_':[28,['pointer', ['uint8']]],

    }],
    'MemMapSpace': [ 0x24 ,{
        'inheritance': [0, ['ContinuousSpace']],
        'mem_map_':[32,['pointer', ['MemMap']]],
    }],
    'ContinuousMemMapAllocSpace':[ 0x34 ,{
        # 'inheritance': [0, ['MemMapSpace']], # khong can dung den
        # 'inheritance': [36, ['AllocSpace']], # khong can dung den
        'live_bitmap_':[40,['pointer', ['accounting::ContinuousSpaceBitmap']]],
        'mark_bitmap_':[44,['pointer', ['accounting::ContinuousSpaceBitmap']]],
        'temp_bitmap_':[48,['pointer', ['accounting::ContinuousSpaceBitmap']]],
    }],
    'MallocSpace' : [0x70 , { #112
        'inheritance': [0, ['ContinuousMemMapAllocSpace']],
     'recent_freed_objects_':[52,['']],
     'recent_free_pos_':[52, ['']],
     'lock_':[56,['']],
     'growth_limit_':[96,['']],
     'can_move_objects_':[100,['']],
     'starting_size_':[104,['']],
     'initial_size_':[108,['']],
    }],
    'RegionSpace' : [ 0xa8, {
        'inheritance': [0, ['ContinuousMemMapAllocSpace']],
        'region_lock_': [56, ['Mutex']],
        'time_': [96, ['uint']],
        'num_regions_': [100, ['size_t']],
        'num_non_free_regions_': [104, ['size_t']],
        'regions_':[ 108,['pointer', ['Array', ['Region']]]],
        'non_free_region_index_limit_': [112, ['size_t']],
        'current_region_': [116, ['pointer', ['Region']]],
        'evac_region_': [120, ['pointer', ['Region']]],
        'full_region_': [124, ['pointer', ['Region']]],
        'mark_bitmap_': [164, ['pointer', ['accounting::ContinuousSpaceBitmap']]],
    }],
    'Region' : [ 0x28, {
        'idx_' : [0, ['size_t']],
        'begin_': [4, ['pointer', ['uint8']]],
        'top_': [8, ['Atomic<uint8_t*>']],
        'end_': [12, ['pointer', ['uint8']]],
        'state_': [16, ['RegionState']],
        'type_': [17, ['RegionType']],
        'objects_allocated_': [20, ['Atomic<size_t>']],
        'alloc_time_': [24, ['uint']],
        'live_bytes_': [28, ['size_t']],
        'is_newly_allocated_': [32, ['boolean']],
        'is_a_tlab_': [33, ['boolean']],
        'thread_': [36, ['pointer', ['Thread']]],
    }],
    'OatFile':[ 0x88 ,{
        '_vptr':[0 ,['pointer', ['virtual']]],
        'location_':[4 ,['std:string']],
        'vdex_':[16, ['pointer', ['VdexFile']]],
        'begin_':[20 ,['pointer', ['uint8']]],
        'end_':[24 ,['pointer', ['uint']]],
        'bss_begin_':[28 ,['pointer', ['uint']]],
        'bss_end_':[32 ,['pointer', ['uint']]],
        'bss_roots_':[36 ,['pointer', ['uint']]],
        'is_executable_':[40 ,['const boolean']],
        'oat_dex_files_storage_':[44 ,['pointer', ['std::vector<const OatDexFile*>']]],
    }],
    'ImageSpace':[0x3c,{
        'inheritance' : [0,['MemMapSpace']],
        'live_bitmap_':[36,['pointer', ['accounting::ContinuousSpaceBitmap']]],
        'oat_file_': [40, ['pointer', ['OatFile']]],
        'oat_file_non_owned_': [44, ['pointer', ['OatFile']]],
        'image_location_': [48, ['std::string']],
    }],
    'SpaceBitmap':[0x1c,{
        'mem_map_':[0,[]],
        'bitmap_begin_':[4,[]],
        'bitmap_size_':[8,[]],
        'heap_begin_':[12,[]],
        'name_':[16, []],
    }],
    'Monitor':[0x60,{
        'monitor_lock_':[0,[]],
        'monitor_contenders_':[40,[]],
        'num_waiters_':[56,[]],
        'owner_':[60,[]],
        'lock_count_':[64, []],
        'obj_':[68, []],
        'wait_set_':[72, []],
        'hash_code_':[76, []],
        'locking_method_':[80, []],
        'locking_dex_pc_':[84, []],
        'monitor_id_':[88, []],
    }],
}

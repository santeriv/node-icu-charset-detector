{
  'targets': [
    {
      'target_name': 'node-icu-charset-detector',
      'sources': [ 'node-icu-charset-detector.cpp' ],
      'include_dirs': ['./lib/headers'],### see ./lib/license.html
      'cflags!': [ '-fno-exceptions', '-D_REENTRANT -I./lib/headers -DU_STATIC_IMPLEMENTATION' ],
      'cflags_cc!': [ '-fno-exceptions' ],
      'libraries': [ '-ldl -lm   -L./lib -licui18n -licuuc -licudata  -ldl -lm' ],
      'conditions': [
        ['OS=="mac"', {
          'include_dirs': [
              '/opt/local/include'
          ],
          'xcode_settings': {
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
          }
        }]
      ]
    }
  ]
}

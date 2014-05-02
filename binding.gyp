{
  'targets': [
    {
      'target_name': 'node-icu-charset-detector',
      'sources': [ 'node-icu-charset-detector.cpp' ],
      'include_dirs': ['./icu/include'],### see ./icu/license.html
      'cflags': [ '-fPIC -fno-exceptions', '-L./icu/include -DU_STATIC_IMPLEMENTATION' ],
      'cflags_cc': [ '-fPIC -fno-exceptions -DU_STATIC_IMPLEMENTATION' ],
      'libraries': [ '../icu/lib/libicui18n.a ../icu/lib/libicuuc.a ../icu/lib/libicudata.a' ],
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

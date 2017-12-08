"""Generated message classes for testing version v1.

Allows developers to run automated tests for their mobile applications on
Google infrastructure.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding


package = 'testing'


class Account(_messages.Message):
  """Identifies an account and how to log into it

  Fields:
    googleAuto: An automatic google login account
  """

  googleAuto = _messages.MessageField('GoogleAuto', 1)


class AndroidDevice(_messages.Message):
  """A single Android device.

  Fields:
    androidModelId: The id of the Android device to be used. Use the
      EnvironmentDiscoveryService to get supported options. Required
    androidVersionId: The id of the Android OS version to be used. Use the
      EnvironmentDiscoveryService to get supported options. Required
    locale: The locale the test device used for testing. Use the
      EnvironmentDiscoveryService to get supported options. Required
    orientation: How the device is oriented during the test. Use the
      EnvironmentDiscoveryService to get supported options. Required
  """

  androidModelId = _messages.StringField(1)
  androidVersionId = _messages.StringField(2)
  locale = _messages.StringField(3)
  orientation = _messages.StringField(4)


class AndroidDeviceCatalog(_messages.Message):
  """The currently supported Android devices.

  Fields:
    models: The set of supported Android device models. @OutputOnly
    runtimeConfiguration: The set of supported runtime configurations.
      @OutputOnly
    versions: The set of supported Android OS versions. @OutputOnly
  """

  models = _messages.MessageField('AndroidModel', 1, repeated=True)
  runtimeConfiguration = _messages.MessageField('AndroidRuntimeConfiguration', 2)
  versions = _messages.MessageField('AndroidVersion', 3, repeated=True)


class AndroidInstrumentationTest(_messages.Message):
  """A test of an Android application that can control an Android component
  independently of its normal lifecycle. Android instrumentation tests run an
  application APK and test APK inside the same process on a virtual or
  physical AndroidDevice.  They also specify a test runner class, such as
  com.google.GoogleTestRunner, which can vary on the specific instrumentation
  framework chosen.  See
  <http://developer.android.com/tools/testing/testing_android.html> for more
  information on types of Android tests.

  Fields:
    appApk: The APK for the application under test. Required
    appPackageId: The java package for the application under test. Optional,
      default is determined by examining the application's manifest.
    testApk: The APK containing the test code to be executed. Required
    testPackageId: The java package for the test to be executed. Optional,
      default is determined by examining the application's manifest.
    testRunnerClass: The InstrumentationTestRunner class. Optional, default is
      determined by examining the application's manifest.
    testTargets: Each target must be fully qualified with the package name or
      class name, in one of these formats:  - "package package_name"  - "class
      package_name.class_name"  - "class package_name.class_name#method_name"
      Optional, if empty, all targets in the module will be run.
  """

  appApk = _messages.MessageField('FileReference', 1)
  appPackageId = _messages.StringField(2)
  testApk = _messages.MessageField('FileReference', 3)
  testPackageId = _messages.StringField(4)
  testRunnerClass = _messages.StringField(5)
  testTargets = _messages.StringField(6, repeated=True)


class AndroidMatrix(_messages.Message):
  """A set of Android device configuration permutations is defined by the the
  cross-product of the given axes.  Internally, the given AndroidMatrix will
  be expanded into a set of AndroidDevices.  Only supported permutations will
  be instantiated.  Invalid permutations (e.g., incompatible models/versions)
  are ignored.

  Fields:
    androidModelIds: The ids of the set of Android device to be used. Use the
      EnvironmentDiscoveryService to get supported options. Required
    androidVersionIds: The ids of the set of Android OS version to be used.
      Use the EnvironmentDiscoveryService to get supported options. Required
    locales: The set of locales the test device will enable for testing. Use
      the EnvironmentDiscoveryService to get supported options. Required
    orientations: The set of orientations to test with. Use the
      EnvironmentDiscoveryService to get supported options. Required
  """

  androidModelIds = _messages.StringField(1, repeated=True)
  androidVersionIds = _messages.StringField(2, repeated=True)
  locales = _messages.StringField(3, repeated=True)
  orientations = _messages.StringField(4, repeated=True)


class AndroidModel(_messages.Message):
  """A description of an Android device tests may be run on.

  Enums:
    FormValueValuesEnum: Whether this device is virtual or physical.
      @OutputOnly

  Fields:
    brand: The company that this device is branded with. Example: "Google",
      "Samsung" @OutputOnly
    codename: The name of the industrial design. This corresponds to
      android.os.Build.DEVICE @OutputOnly
    form: Whether this device is virtual or physical. @OutputOnly
    id: The unique opaque id for this model. Use this for invoking the
      TestExecutionService. @OutputOnly
    manufacturer: The manufacturer of this device. @OutputOnly
    name: The human-readable marketing name for this device model. Examples:
      "Nexus 5", "Galaxy S5" @OutputOnly
    screenDensity: Screen density in DPI. This corresponds to
      ro.sf.lcd_density @OutputOnly
    screenX: Screen size in the horizontal (X) dimension measured in pixels.
      @OutputOnly
    screenY: Screen size in the vertical (Y) dimension measured in pixels.
      @OutputOnly
    supportedAbis: The list of supported ABIs for this device. This
      corresponds to either android.os.Build.SUPPORTED_ABIS (for API level 21
      and above) or android.os.Build.CPU_ABI/CPU_ABI2. The most preferred ABI
      is the first element in the list.  Elements are optionally prefixed by
      "version_id:" (where version_id is the id of an AndroidVersion),
      denoting an ABI that is supported only on a particular version.
      @OutputOnly
    supportedVersionIds: The set of Android versions this device supports.
      @OutputOnly
    tags: Tags for this dimension. Examples: "default", "preview",
      "deprecated"
  """

  class FormValueValuesEnum(_messages.Enum):
    """Whether this device is virtual or physical. @OutputOnly

    Values:
      DEVICE_FORM_UNSPECIFIED: Do not use.  For proto versioning only.
      VIRTUAL: A software stack that simulates the device
      PHYSICAL: Actual hardware
    """
    DEVICE_FORM_UNSPECIFIED = 0
    VIRTUAL = 1
    PHYSICAL = 2

  brand = _messages.StringField(1)
  codename = _messages.StringField(2)
  form = _messages.EnumField('FormValueValuesEnum', 3)
  id = _messages.StringField(4)
  manufacturer = _messages.StringField(5)
  name = _messages.StringField(6)
  screenDensity = _messages.IntegerField(7, variant=_messages.Variant.INT32)
  screenX = _messages.IntegerField(8, variant=_messages.Variant.INT32)
  screenY = _messages.IntegerField(9, variant=_messages.Variant.INT32)
  supportedAbis = _messages.StringField(10, repeated=True)
  supportedVersionIds = _messages.StringField(11, repeated=True)
  tags = _messages.StringField(12, repeated=True)


class AndroidRoboTest(_messages.Message):
  """A test of an android application that explores the application on a
  virtual or physical Android Device, finding culprits and crashes as it goes.

  Fields:
    appApk: The APK for the application under test. Required
    appInitialActivity: The initial activity that should be used to start the
      app. Optional
    appPackageId: The java package for the application under test. Optional,
      default is determined by examining the application's manifest.
    maxDepth: The max depth of the traversal stack Robo can explore. Needs to
      be at least 2 to make Robo explore the app beyond the first activity.
      Default is 50. Optional
    maxSteps: The max number of steps Robo can execute. Default is no limit.
      Optional
    roboDirectives: A set of directives Robo should apply during the crawl.
      This allows users to customize the crawl. For example, the username and
      password for a test account can be provided. Optional
  """

  appApk = _messages.MessageField('FileReference', 1)
  appInitialActivity = _messages.StringField(2)
  appPackageId = _messages.StringField(3)
  maxDepth = _messages.IntegerField(4, variant=_messages.Variant.INT32)
  maxSteps = _messages.IntegerField(5, variant=_messages.Variant.INT32)
  roboDirectives = _messages.MessageField('RoboDirective', 6, repeated=True)


class AndroidRuntimeConfiguration(_messages.Message):
  """Configuration that can be selected at the time a test is run.

  Fields:
    locales: The set of available locales. @OutputOnly
    orientations: The set of available orientations. @OutputOnly
  """

  locales = _messages.MessageField('Locale', 1, repeated=True)
  orientations = _messages.MessageField('Orientation', 2, repeated=True)


class AndroidVersion(_messages.Message):
  """A version of the Android OS

  Fields:
    apiLevel: The API level for this Android version. Examples: 18, 19
      @OutputOnly
    codeName: The code name for this Android version. Examples: "JellyBean",
      "KitKat" @OutputOnly
    distribution: Market share for this version. @OutputOnly
    id: An opaque id for this Android version. Use this id to invoke the
      TestExecutionService. @OutputOnly
    releaseDate: The date this Android version became available in the market.
      @OutputOnly
    tags: Tags for this dimension. Examples: "default", "preview",
      "deprecated"
    versionString: A string representing this version of the Android OS.
      Examples: "4.3", "4.4" @OutputOnly
  """

  apiLevel = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  codeName = _messages.StringField(2)
  distribution = _messages.MessageField('Distribution', 3)
  id = _messages.StringField(4)
  releaseDate = _messages.MessageField('Date', 5)
  tags = _messages.StringField(6, repeated=True)
  versionString = _messages.StringField(7)


class CancelTestMatrixResponse(_messages.Message):
  """Response containing the current state of the specified test matrix.

  Enums:
    TestStateValueValuesEnum: The current rolled-up state of the test matrix.
      If this state is already final, then the cancelation request will have
      no effect.

  Fields:
    testState: The current rolled-up state of the test matrix. If this state
      is already final, then the cancelation request will have no effect.
  """

  class TestStateValueValuesEnum(_messages.Enum):
    """The current rolled-up state of the test matrix. If this state is
    already final, then the cancelation request will have no effect.

    Values:
      TEST_STATE_UNSPECIFIED: Do not use.  For proto versioning only.
      VALIDATING: The execution or matrix is being validated.
      PENDING: The execution or matrix is waiting for resources to become
        available.
      RUNNING: The execution is currently being processed.  Can only be set on
        an execution.
      FINISHED: The execution or matrix has terminated normally.  On a matrix
        this means that the matrix level processing completed normally, but
        individual executions may be in an ERROR state.
      ERROR: The execution or matrix has stopped because it encountered an
        infrastructure failure.
      UNSUPPORTED_ENVIRONMENT: The execution was not run because it
        corresponds to a unsupported environment.  Can only be set on an
        execution.
      INCOMPATIBLE_ENVIRONMENT: The execution was not run because the provided
        inputs are incompatible with the requested environment.  Example:
        requested AndroidVersion is lower than APK's minSdkVersion  Can only
        be set on an execution.
      INCOMPATIBLE_ARCHITECTURE: The execution was not run because the
        provided inputs are incompatible with the requested architecture.
        Example: requested device does not support running the native code in
        the supplied APK  Can only be set on an execution.
      CANCELLED: The user cancelled the execution.  Can only be set on an
        execution.
      INVALID: The execution or matrix was not run because the provided inputs
        are not valid.  Examples: input file is not of the expected type, is
        malformed/corrupt, or was flagged as malware
    """
    TEST_STATE_UNSPECIFIED = 0
    VALIDATING = 1
    PENDING = 2
    RUNNING = 3
    FINISHED = 4
    ERROR = 5
    UNSUPPORTED_ENVIRONMENT = 6
    INCOMPATIBLE_ENVIRONMENT = 7
    INCOMPATIBLE_ARCHITECTURE = 8
    CANCELLED = 9
    INVALID = 10

  testState = _messages.EnumField('TestStateValueValuesEnum', 1)


class ClientInfo(_messages.Message):
  """Information about the client which invoked the test.

  Fields:
    name: Client name, such as gcloud. Required
  """

  name = _messages.StringField(1)


class Date(_messages.Message):
  """Represents a whole calendar date, e.g. date of birth. The time of day and
  time zone are either specified elsewhere or are not significant. The date is
  relative to the Proleptic Gregorian Calendar. The day may be 0 to represent
  a year and month where the day is not significant, e.g. credit card
  expiration date. The year may be 0 to represent a month and day independent
  of year, e.g. anniversary date. Related types are google.type.TimeOfDay and
  `google.protobuf.Timestamp`.

  Fields:
    day: Day of month. Must be from 1 to 31 and valid for the year and month,
      or 0 if specifying a year/month where the day is not significant.
    month: Month of year. Must be from 1 to 12.
    year: Year of date. Must be from 1 to 9999, or 0 if specifying a date
      without a year.
  """

  day = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  month = _messages.IntegerField(2, variant=_messages.Variant.INT32)
  year = _messages.IntegerField(3, variant=_messages.Variant.INT32)


class DeviceFile(_messages.Message):
  """A single device file description.

  Fields:
    obbFile: A reference to an opaque binary blob file
  """

  obbFile = _messages.MessageField('ObbFile', 1)


class Distribution(_messages.Message):
  """Data about the relative number of devices running a given configuration
  of the Android platform.

  Fields:
    marketShare: The estimated fraction (0-1) of the total market with this
      configuration. @OutputOnly
    measurementTime: The time this distribution was measured. @OutputOnly
  """

  marketShare = _messages.FloatField(1)
  measurementTime = _messages.StringField(2)


class Empty(_messages.Message):
  """A generic empty message that you can re-use to avoid defining duplicated
  empty messages in your APIs. A typical example is to use it as the request
  or the response type of an API method. For instance:      service Foo {
  rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty);     }  The
  JSON representation for `Empty` is empty JSON object `{}`.
  """



class Environment(_messages.Message):
  """The environment in which the test is run.

  Fields:
    androidDevice: An Android device which must be used with an Android test.
  """

  androidDevice = _messages.MessageField('AndroidDevice', 1)


class EnvironmentMatrix(_messages.Message):
  """The matrix of environments in which the test is to be executed.

  Fields:
    androidMatrix: A matrix of Android devices.
  """

  androidMatrix = _messages.MessageField('AndroidMatrix', 1)


class EnvironmentVariable(_messages.Message):
  """A key-value pair passed as an environment variable to the test

  Fields:
    key: Key for the environment variable
    value: Value for the environment variable
  """

  key = _messages.StringField(1)
  value = _messages.StringField(2)


class FileReference(_messages.Message):
  """A reference to a file, used for user inputs.

  Fields:
    gcsPath: A path to a file in Google Cloud Storage. Example: gs://build-
      app-1414623860166/app-debug-unaligned.apk
  """

  gcsPath = _messages.StringField(1)


class GoogleAuto(_messages.Message):
  """Enables automatic Google account login. If set, the service will
  automatically generate a Google test account and add it to the device,
  before executing the test. Note that test accounts might be reused. Many
  applications show their full set of functionalities when an account is
  present on the device. Logging into the device with these generated accounts
  allows testing more functionalities.
  """



class GoogleCloudStorage(_messages.Message):
  """A storage location within Google cloud storage (GCS).

  Fields:
    gcsPath: The path to a directory in GCS that will eventually contain the
      results for this test. The requesting user must have write access on the
      bucket in the supplied path. Required
  """

  gcsPath = _messages.StringField(1)


class ListTestMatricesResponse(_messages.Message):
  """Response contain a list of Test Matrices.

  Fields:
    testMatrices: The set of test matrices.
  """

  testMatrices = _messages.MessageField('TestMatrix', 1, repeated=True)


class Locale(_messages.Message):
  """A location/region designation for language.

  Fields:
    id: The id for this locale. Example: "en_US" @OutputOnly
    name: A human-friendly name for this language/locale. Example: "English"
      @OutputOnly
    region: A human-friendy string representing the region for this locale.
      Example: "United States" Not present for every locale. @OutputOnly
    tags: Tags for this dimension. Examples: "default"
  """

  id = _messages.StringField(1)
  name = _messages.StringField(2)
  region = _messages.StringField(3)
  tags = _messages.StringField(4, repeated=True)


class ObbFile(_messages.Message):
  """An opaque binary blob file to install on the device before the test
  starts

  Fields:
    obb: Opaque Binary Blob (OBB) file(s) to install on the device Required
    obbFileName: OBB file name which must conform to the format as specified
      by Android e.g. [main|patch].0300110.com.example.android.obb which will
      be installed into   <shared-storage>/Android/obb/<package-name>/ on the
      device Required
  """

  obb = _messages.MessageField('FileReference', 1)
  obbFileName = _messages.StringField(2)


class Orientation(_messages.Message):
  """Screen orientation of the device.

  Fields:
    id: The id for this orientation. Example: "portrait" @OutputOnly
    name: A human-friendly name for this orientation. Example: "portrait"
      @OutputOnly
    tags: Tags for this dimension. Examples: "default"
  """

  id = _messages.StringField(1)
  name = _messages.StringField(2)
  tags = _messages.StringField(3, repeated=True)


class ResultStorage(_messages.Message):
  """Locations where the results of running the test are stored.

  Fields:
    googleCloudStorage: Required.
    toolResultsExecution: The tool results execution that results are written
      to. @OutputOnly
    toolResultsHistory: The tool results history that contains the tool
      results execution that results are written to.  Optional, if not
      provided the service will choose an appropriate value.
  """

  googleCloudStorage = _messages.MessageField('GoogleCloudStorage', 1)
  toolResultsExecution = _messages.MessageField('ToolResultsExecution', 2)
  toolResultsHistory = _messages.MessageField('ToolResultsHistory', 3)


class RoboDirective(_messages.Message):
  """Directs Robo to interact with a specific UI element if it is encountered
  during the crawl. Currently, Robo can perform text entry or element click.

  Fields:
    inputText: The text that Robo is directed to set. If left empty, the
      directive will be treated as a CLICK on the element matching the
      resource_name.
    resourceName: The android resource name of the target UI element For
      example,    in Java: R.string.foo    in xml: @string/foo Only the \u201cfoo\u201d
      part is needed. Reference doc:
      https://developer.android.com/guide/topics/resources/accessing-
      resources.html Required
  """

  inputText = _messages.StringField(1)
  resourceName = _messages.StringField(2)


class StandardQueryParameters(_messages.Message):
  """Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    bearer_token: OAuth bearer token.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    pp: Pretty-print response.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    """Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    """V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default=u'json')
  bearer_token = _messages.StringField(4)
  callback = _messages.StringField(5)
  fields = _messages.StringField(6)
  key = _messages.StringField(7)
  oauth_token = _messages.StringField(8)
  pp = _messages.BooleanField(9, default=True)
  prettyPrint = _messages.BooleanField(10, default=True)
  quotaUser = _messages.StringField(11)
  trace = _messages.StringField(12)
  uploadType = _messages.StringField(13)
  upload_protocol = _messages.StringField(14)


class TestDetails(_messages.Message):
  """Additional details about the progress of the running test.

  Fields:
    errorMessage: If the TestState is ERROR, then this string will contain
      human-readable details about the error. @OutputOnly
    progressMessages: Human-readable, detailed descriptions of the test's
      progress. For example: "Provisioning a device", "Starting Test".  During
      the course of execution new data may be appended to the end of
      progress_messages. @OutputOnly
  """

  errorMessage = _messages.StringField(1)
  progressMessages = _messages.StringField(2, repeated=True)


class TestEnvironmentCatalog(_messages.Message):
  """A description of a test environment.

  Fields:
    androidDeviceCatalog: Android devices suitable for running Android
      Instrumentation Tests.
  """

  androidDeviceCatalog = _messages.MessageField('AndroidDeviceCatalog', 1)


class TestExecution(_messages.Message):
  """Specifies a single test to be executed in a single environment.

  Enums:
    StateValueValuesEnum: Indicates the current progress of the test execution
      (e.g., FINISHED). @OutputOnly

  Fields:
    environment: How the host machine(s) are configured. @OutputOnly
    id: Unique id set by the backend. @OutputOnly
    matrixId: Id of the containing TestMatrix. @OutputOnly
    projectId: The cloud project that owns the test execution. @OutputOnly
    state: Indicates the current progress of the test execution (e.g.,
      FINISHED). @OutputOnly
    testDetails: Additional details about the running test. @OutputOnly
    testSpecification: How to run the test. @OutputOnly
    timestamp: The time this test execution was initially created. @OutputOnly
    toolResultsStep: Where the results for this execution are written.
      @OutputOnly
  """

  class StateValueValuesEnum(_messages.Enum):
    """Indicates the current progress of the test execution (e.g., FINISHED).
    @OutputOnly

    Values:
      TEST_STATE_UNSPECIFIED: Do not use.  For proto versioning only.
      VALIDATING: The execution or matrix is being validated.
      PENDING: The execution or matrix is waiting for resources to become
        available.
      RUNNING: The execution is currently being processed.  Can only be set on
        an execution.
      FINISHED: The execution or matrix has terminated normally.  On a matrix
        this means that the matrix level processing completed normally, but
        individual executions may be in an ERROR state.
      ERROR: The execution or matrix has stopped because it encountered an
        infrastructure failure.
      UNSUPPORTED_ENVIRONMENT: The execution was not run because it
        corresponds to a unsupported environment.  Can only be set on an
        execution.
      INCOMPATIBLE_ENVIRONMENT: The execution was not run because the provided
        inputs are incompatible with the requested environment.  Example:
        requested AndroidVersion is lower than APK's minSdkVersion  Can only
        be set on an execution.
      INCOMPATIBLE_ARCHITECTURE: The execution was not run because the
        provided inputs are incompatible with the requested architecture.
        Example: requested device does not support running the native code in
        the supplied APK  Can only be set on an execution.
      CANCELLED: The user cancelled the execution.  Can only be set on an
        execution.
      INVALID: The execution or matrix was not run because the provided inputs
        are not valid.  Examples: input file is not of the expected type, is
        malformed/corrupt, or was flagged as malware
    """
    TEST_STATE_UNSPECIFIED = 0
    VALIDATING = 1
    PENDING = 2
    RUNNING = 3
    FINISHED = 4
    ERROR = 5
    UNSUPPORTED_ENVIRONMENT = 6
    INCOMPATIBLE_ENVIRONMENT = 7
    INCOMPATIBLE_ARCHITECTURE = 8
    CANCELLED = 9
    INVALID = 10

  environment = _messages.MessageField('Environment', 1)
  id = _messages.StringField(2)
  matrixId = _messages.StringField(3)
  projectId = _messages.StringField(4)
  state = _messages.EnumField('StateValueValuesEnum', 5)
  testDetails = _messages.MessageField('TestDetails', 6)
  testSpecification = _messages.MessageField('TestSpecification', 7)
  timestamp = _messages.StringField(8)
  toolResultsStep = _messages.MessageField('ToolResultsStep', 9)


class TestMatrix(_messages.Message):
  """A group of one or more TestExecutions, built by taking a product of
  values over a pre-defined set of axes.

  Enums:
    InvalidMatrixDetailsValueValuesEnum: Describes why the matrix is
      considered invalid. Only useful for matrices in the INVALID state.
      @OutputOnly
    StateValueValuesEnum: Indicates the current progress of the test matrix
      (e.g., FINISHED) @OutputOnly

  Fields:
    clientInfo: Information about the client which invoked the test. Optional
    environmentMatrix: How the host machine(s) are configured. Required
    invalidMatrixDetails: Describes why the matrix is considered invalid. Only
      useful for matrices in the INVALID state. @OutputOnly
    projectId: The cloud project that owns the test matrix. @OutputOnly
    resultStorage: Where the results for the matrix are written. Required
    state: Indicates the current progress of the test matrix (e.g., FINISHED)
      @OutputOnly
    testExecutions: The list of test executions that the service creates for
      this matrix. @OutputOnly
    testMatrixId: Unique id set by the service. @OutputOnly
    testSpecification: How to run the test. Required
    timestamp: The time this test matrix was initially created. @OutputOnly
  """

  class InvalidMatrixDetailsValueValuesEnum(_messages.Enum):
    """Describes why the matrix is considered invalid. Only useful for
    matrices in the INVALID state. @OutputOnly

    Values:
      INVALID_MATRIX_DETAILS_UNSPECIFIED: Do not use. For proto versioning
        only.
      DETAILS_UNAVAILABLE: The matrix is INVALID, but there are no further
        details available.
      MALFORMED_APK: The input app APK could not be parsed.
      MALFORMED_TEST_APK: The input test APK could not be parsed.
      NO_MANIFEST: The AndroidManifest.xml could not be found.
      NO_PACKAGE_NAME: The APK manifest does not declare a package name.
      TEST_SAME_AS_APP: The test package and app package are the same.
      NO_INSTRUMENTATION: The test apk does not declare an instrumentation.
      NO_LAUNCHER_ACTIVITY: A main launcher activity could not be found.
      FORBIDDEN_PERMISSIONS: The app declares one or more permissions that are
        not allowed.
      INVALID_ROBO_DIRECTIVES: There is a conflict in the provided
        robo_directives.
    """
    INVALID_MATRIX_DETAILS_UNSPECIFIED = 0
    DETAILS_UNAVAILABLE = 1
    MALFORMED_APK = 2
    MALFORMED_TEST_APK = 3
    NO_MANIFEST = 4
    NO_PACKAGE_NAME = 5
    TEST_SAME_AS_APP = 6
    NO_INSTRUMENTATION = 7
    NO_LAUNCHER_ACTIVITY = 8
    FORBIDDEN_PERMISSIONS = 9
    INVALID_ROBO_DIRECTIVES = 10

  class StateValueValuesEnum(_messages.Enum):
    """Indicates the current progress of the test matrix (e.g., FINISHED)
    @OutputOnly

    Values:
      TEST_STATE_UNSPECIFIED: Do not use.  For proto versioning only.
      VALIDATING: The execution or matrix is being validated.
      PENDING: The execution or matrix is waiting for resources to become
        available.
      RUNNING: The execution is currently being processed.  Can only be set on
        an execution.
      FINISHED: The execution or matrix has terminated normally.  On a matrix
        this means that the matrix level processing completed normally, but
        individual executions may be in an ERROR state.
      ERROR: The execution or matrix has stopped because it encountered an
        infrastructure failure.
      UNSUPPORTED_ENVIRONMENT: The execution was not run because it
        corresponds to a unsupported environment.  Can only be set on an
        execution.
      INCOMPATIBLE_ENVIRONMENT: The execution was not run because the provided
        inputs are incompatible with the requested environment.  Example:
        requested AndroidVersion is lower than APK's minSdkVersion  Can only
        be set on an execution.
      INCOMPATIBLE_ARCHITECTURE: The execution was not run because the
        provided inputs are incompatible with the requested architecture.
        Example: requested device does not support running the native code in
        the supplied APK  Can only be set on an execution.
      CANCELLED: The user cancelled the execution.  Can only be set on an
        execution.
      INVALID: The execution or matrix was not run because the provided inputs
        are not valid.  Examples: input file is not of the expected type, is
        malformed/corrupt, or was flagged as malware
    """
    TEST_STATE_UNSPECIFIED = 0
    VALIDATING = 1
    PENDING = 2
    RUNNING = 3
    FINISHED = 4
    ERROR = 5
    UNSUPPORTED_ENVIRONMENT = 6
    INCOMPATIBLE_ENVIRONMENT = 7
    INCOMPATIBLE_ARCHITECTURE = 8
    CANCELLED = 9
    INVALID = 10

  clientInfo = _messages.MessageField('ClientInfo', 1)
  environmentMatrix = _messages.MessageField('EnvironmentMatrix', 2)
  invalidMatrixDetails = _messages.EnumField('InvalidMatrixDetailsValueValuesEnum', 3)
  projectId = _messages.StringField(4)
  resultStorage = _messages.MessageField('ResultStorage', 5)
  state = _messages.EnumField('StateValueValuesEnum', 6)
  testExecutions = _messages.MessageField('TestExecution', 7, repeated=True)
  testMatrixId = _messages.StringField(8)
  testSpecification = _messages.MessageField('TestSpecification', 9)
  timestamp = _messages.StringField(10)


class TestSetup(_messages.Message):
  """A description of how to set up the device prior to running the test

  Fields:
    account: The device will be logged in on this account for the duration of
      the test. Optional
    directoriesToPull: The directories on the device to upload to GCS at the
      end of the test; they must be absolute, whitelisted paths. Refer to
      RegularFile for whitelisted paths. Optional
    environmentVariables: Environment variables to set for the test (only
      applicable for instrumentation tests).
    filesToPush: Optional
  """

  account = _messages.MessageField('Account', 1)
  directoriesToPull = _messages.StringField(2, repeated=True)
  environmentVariables = _messages.MessageField('EnvironmentVariable', 3, repeated=True)
  filesToPush = _messages.MessageField('DeviceFile', 4, repeated=True)


class TestSpecification(_messages.Message):
  """A description of how to run the test.

  Fields:
    androidInstrumentationTest: An Android instrumentation test.
    androidRoboTest: An Android robo test.
    autoGoogleLogin: Enables automatic Google account login. If set, the
      service will automatically generate a Google test account and add it to
      the device, before executing the test. Note that test accounts might be
      reused. Many applications show their full set of functionalities when an
      account is present on the device. Logging into the device with these
      generated accounts allows testing more functionalities. Default is
      false. Optional
    testSetup: Test setup requirements e.g. files to install, bootstrap
      scripts Optional
    testTimeout: Max time a test execution is allowed to run before it is
      automatically cancelled. Optional, default is 5 min.
  """

  androidInstrumentationTest = _messages.MessageField('AndroidInstrumentationTest', 1)
  androidRoboTest = _messages.MessageField('AndroidRoboTest', 2)
  autoGoogleLogin = _messages.BooleanField(3)
  testSetup = _messages.MessageField('TestSetup', 4)
  testTimeout = _messages.StringField(5)


class TestingProjectsTestMatricesCancelRequest(_messages.Message):
  """A TestingProjectsTestMatricesCancelRequest object.

  Fields:
    projectId: Cloud project that owns the test.
    testMatrixId: Test matrix that will be canceled.
  """

  projectId = _messages.StringField(1, required=True)
  testMatrixId = _messages.StringField(2, required=True)


class TestingProjectsTestMatricesCreateRequest(_messages.Message):
  """A TestingProjectsTestMatricesCreateRequest object.

  Fields:
    projectId: The GCE project under which this job will run.
    requestId: A string id used to detect duplicated requests. Ids are
      automatically scoped to a project, so users should ensure the ID is
      unique per-project. A UUID is recommended.  Optional, but strongly
      recommended.
    testMatrix: A TestMatrix resource to be passed as the request body.
  """

  projectId = _messages.StringField(1, required=True)
  requestId = _messages.StringField(2)
  testMatrix = _messages.MessageField('TestMatrix', 3)


class TestingProjectsTestMatricesDeleteRequest(_messages.Message):
  """A TestingProjectsTestMatricesDeleteRequest object.

  Fields:
    projectId: Cloud project that owns the test.
    testMatrixId: Test matrix that will be canceled.
  """

  projectId = _messages.StringField(1, required=True)
  testMatrixId = _messages.StringField(2, required=True)


class TestingProjectsTestMatricesGetRequest(_messages.Message):
  """A TestingProjectsTestMatricesGetRequest object.

  Fields:
    projectId: Cloud project that owns the test matrix.
    testMatrixId: Unique test matrix id which was assigned by the service.
  """

  projectId = _messages.StringField(1, required=True)
  testMatrixId = _messages.StringField(2, required=True)


class TestingProjectsTestMatricesListRequest(_messages.Message):
  """A TestingProjectsTestMatricesListRequest object.

  Fields:
    projectId: Cloud project that owns the tests.
  """

  projectId = _messages.StringField(1, required=True)


class TestingTestEnvironmentCatalogGetRequest(_messages.Message):
  """A TestingTestEnvironmentCatalogGetRequest object.

  Enums:
    EnvironmentTypeValueValuesEnum: The type of environment that should be
      listed.

  Fields:
    environmentType: The type of environment that should be listed.
  """

  class EnvironmentTypeValueValuesEnum(_messages.Enum):
    """The type of environment that should be listed.

    Values:
      ENVIRONMENT_TYPE_UNSPECIFIED: <no description>
      ANDROID: <no description>
    """
    ENVIRONMENT_TYPE_UNSPECIFIED = 0
    ANDROID = 1

  environmentType = _messages.EnumField('EnvironmentTypeValueValuesEnum', 1, required=True)


class ToolResultsExecution(_messages.Message):
  """Represents a tool results execution resource.  This has the results of a
  TestMatrix.

  Fields:
    executionId: A tool results execution ID. @OutputOnly
    historyId: A tool results history ID. @OutputOnly
    projectId: The cloud project that owns the tool results execution.
      @OutputOnly
  """

  executionId = _messages.StringField(1)
  historyId = _messages.StringField(2)
  projectId = _messages.StringField(3)


class ToolResultsHistory(_messages.Message):
  """Represents a tool results history resource.

  Fields:
    historyId: A tool results history ID. Required
    projectId: The cloud project that owns the tool results history. Required
  """

  historyId = _messages.StringField(1)
  projectId = _messages.StringField(2)


class ToolResultsStep(_messages.Message):
  """Represents a tool results step resource.  This has the results of a
  TestExecution.

  Fields:
    executionId: A tool results execution ID. @OutputOnly
    historyId: A tool results history ID. @OutputOnly
    projectId: The cloud project that owns the tool results step. @OutputOnly
    stepId: A tool results step ID. @OutputOnly
  """

  executionId = _messages.StringField(1)
  historyId = _messages.StringField(2)
  projectId = _messages.StringField(3)
  stepId = _messages.StringField(4)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv',
    package=u'testing')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1',
    package=u'testing')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2',
    package=u'testing')
